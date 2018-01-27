from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re,bcrypt
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class TripManager(models.Manager):
	def newtrip(self, plan_maker,destination,desc,start,end,):
		errors = []
		if (len(destination) == 0) or (len(desc) == 0):
			errors.append("Cannot be blank")
		elif (len(destination) == 20) or (len(desc) == 20):
			errors.append("Input is too long")
		elif (start > end):
			errors.append("You can't schedule that! MM/DD/YYYY")
		if len(errors) is not 0:
			return (False, errors)
		else:
			new_trip = Trip.objects.create(plan_maker=User.objects.get(name=plan_maker),destination=destination,desc=desc,start=start,end=end)
		return (True, new_trip)
	def tag_along(self, id, me):
		trip = Trip.objects.get(id=id)
		trip.others.add(User.objects.get(id=me))

class UserManager(models.Manager):
	def register(self, name, username, email, password, confirm_password):
		errors = []
		if (len(name) == 0) or (len(username) == 0)  or (len(email) == 0) or (len(password) == 0):
			errors.append("Cannot be blank")
		elif (not emailRegex.match(email)) or (not nameRegex.match(name)):
			errors.append("Invalid input")
		elif (not (password == confirm_password)):
			errors.append("Password don't match")
		if len(errors) is not 0:
			return (False, errors)
		else:
			new_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			new_user = User.objects.create(name=name, username=username, email=email, password=new_pw)

		return (True, new_user)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()

class Trip(models.Model):
	plan_maker = models.ForeignKey(User, related_name="justme")
	destination = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)
	start = models.DateTimeField(default=datetime.now(), editable=True)
	end = models.DateTimeField(default=datetime.now(), editable=True)
	others = models.ManyToManyField(User,related_name="others")
	objects = TripManager()