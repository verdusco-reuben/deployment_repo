from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)

class Review(models.Model):
	book = models.ForeignKey(Book)
	reviewed_by = models.ForeignKey(User)
	rating = models.IntegerField()
	reviewed_content = models.CharField(max_length=256)
