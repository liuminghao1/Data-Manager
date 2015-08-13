from django.db import models
from django.contrib import admin

class Category(models.Model):
	name = models.CharField(max_length=128,blank=True)
	def __unicode__(self):
		return self.name

class Blog(models.Model):
	title = models.CharField(max_length=128)
	update_time = models.DateTimeField(auto_now=True)
	body = models.TextField()
	category = models.ForeignKey(Category)
	def __unicode__(self):
		return self.title

class Message(models.Model):
	author=models.CharField(max_length=30)
	update_time = models.DateTimeField(auto_now=True)
	body = models.TextField()
	def __unicode__(self):
		return self.author

