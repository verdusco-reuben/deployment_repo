from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re,bcrypt

class TripManager(models.Manager):
	def newtrip(self, plan_maker,destination,desc,start,end):
		errors = []
		if (len(destination) == 0) or (len(desc) == 0) or (len(start) == 0) or (len(end) == 0):
			errors.append("Cannot be blank")
		elif (len(destination) >= 20) or (len(desc) >= 20):
			errors.append("Input is too long")
		elif (start > end):
			errors.append("You can't schedule that! That's start before end")
		if len(errors) is not 0:
			return (False, errors)
		else:
			new_trip = Trip.objects.create(plan_maker=User.objects.get(id=plan_maker),destination=destination,desc=desc,start=start,end=end)
			new_trip.others.add(User.objects.get(id=plan_maker))
			return (True, new_trip)
	def tag_along(self, id, me):
		trip = Trip.objects.get(id=id)
		trip.others.add(User.objects.get(id=me))

	def homepage(self, id):
		try:
			context = {
				'trip' : Trip.objects.filter(others__id=id),
				'notme' : Trip.objects.exclude(others__id=id)
				}
				#help getting taken off bottom table, placed on top

		except:#if they have nothing scheduled!
			context = {
				'me' : Trip.objects.filter(id=request.session['id']),
				'notme' : Trip.objects.all()
				}
		return context
	def destination(self, id, myid):
		user = Trip.objects.get(id=id)
		context = {
			'users' : user,
			'posers' : User.objects.filter(others__id=id).exclude(id=myid)
		}
		return context

class UserManager(models.Manager):
	def register(self, name, username, password, confirm_password):
		errors = []
		if (len(name) == 0) or (len(username) == 0) or (len(password) == 0):
			errors.append("Cannot be blank")
		elif (len(name) < 3) or (len(username) < 3) or (len(password) < 3):
			errors.append("Cannot be less than 8 characters")
		elif (not (password == confirm_password)):
			errors.append("Password don't match")
		if len(errors) is not 0:
			return (False, errors)
		else:
			new_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			new_user = User.objects.create(name=name, username=username, password=new_pw)
			return (True, new_user)
	def login(self, username, password):
		errors = []
		try:
			b = User.objects.get(username=username)
			if bcrypt.checkpw(password.encode(), (b.password).encode()) == True:
				return (True, b)
		except:
			errors.append("Username/Password is invalid")
			return (False, errors)

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Trip(models.Model):
	plan_maker = models.ForeignKey(User, related_name="justme")
	destination = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)
	start = models.DateField()
	end = models.DateField()
	others = models.ManyToManyField(User,related_name="others")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TripManager()
