#-*- coding: utf-8 -*-
#场景 区域 店铺
from django.db import models

# Create your models here.

class Scenc(models.Model):
	scenc_name = models.CharField(max_length=30,unique=True)
	def __unicode__(self):
		return self.scenc_name
class Area(models.Model):
	scenc = models.ForeignKey(Scenc)
	area_name = models.CharField(max_length=30)
	linkman = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	def __unicode__(self):
		return self.area_name
class Shop(models.Model):
	area = models.ForeignKey(Area)
	shop_name = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	number = models.CharField(max_length=30)
	remake = models.CharField(max_length=90)
	linkman  = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	def __unicode__(self):
		return self.shop_name
