#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tba_user(models.Model):
	user = models.OneToOneField(User)
	nickname = models.CharField(max_length=30,)
	ssex = models.CharField(choices=(("M","男"),("F","女")),max_length=5)
	image = models.ImageField(upload_to="media")
	def __unicode__(self):
		return self.user

class Send_card(models.Model):
	tba_user = models.ForeignKey(Tba_user)
	title  = models.CharField(max_length=200)
	cardcontent = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title

class Follow_card(models.Model):
	tba_user = models.ForeignKey(Tba_user)	
	send_card = models.ForeignKey(Send_card)
	followcontent = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.tba_user
