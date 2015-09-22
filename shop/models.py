#-*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# 成就  任务  分数  类别

class Achievement(models.Model):
	task = models.CharField(max_length = 50 )
	score = models.IntegerField(blank = False)
	category = models.CharField(max_length = 10)

# 要求   消费   分数
class Desire(models.Model):
	consume = models.CharField(max_length = 50 )
	score = models.IntegerField(blank = False)

#用户  分数   事件 时间

class Shop_User(models.Model):
	score = models.IntegerField(blank = False)
	evevt = models.CharField(max_length = 50)
	times = models.DateTimeField(auto_now=True)

	
