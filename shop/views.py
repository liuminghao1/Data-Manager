# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from shop.models import Achievement, Desire,Shop_User
from shop.forms import AchievementForm
# Create your views here.

 
def add_score(request):
	s_id = None
	if request.method =='GET':
		s_id = request.GET['score_id']
		t_id = request.GET['task_id']
		print "t_id is ",t_id
	new_s = 0
	if s_id :
		users = Shop_User.objects.order_by('-id')[0]
		print users
		if users:
			new_s = users.score + 1
			print "new_s is ",
			new_u = Shop_User(score = new_s,evevt = t_id)
			new_u.save()
	return HttpResponse(new_s)
	
def tasks(request):
	form = {}
	form['Achievements'] = Achievement.objects.all()
	return render(request,'shop/show_tasks.html',form)

def addtasks(request):
	if request.method == 'POST':
		form = AchievementForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
			return  tasks(request)
		else:
			print form.errors
	else:	
		form = AchievementForm()
	return render(request,'shop/add_tasks.html',{'form':form})


def users(request):
	form = {}
	form['scores'] = Shop_User.objects.all()[0]
	return render(request,'shop/users.html',form)
