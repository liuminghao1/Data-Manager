from django.db import models

#-*- coding: utf-8 -*-
class Books(models.Model):
	book_name = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
class Students(models.Model):
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)	

class  Borrow(models.Model):
	books = models.ForeignKey(Books)
	students = models.ForeignKey(Students)
	loan_data = models.DateTimeField(auto_now=True)
	return_data = models.DateTimeField(auto_now=True)
