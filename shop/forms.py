# _*_ coding: utf-8 _*_
from django import forms
from shop.models import Achievement, Desire,Shop_User

class AchievementForm(forms.ModelForm):
	task = forms.CharField(max_length=50,help_text="任务")
	score = forms.IntegerField(help_text="分数")
	category = forms.CharField(max_length=50,help_text = "类别")
	class Meta:
		model =  Achievement
		fields=('task','score','category')

class Shop_UserForm(forms.ModelForm):
	score = forms.IntegerField(help_text="分数")
	evevt = forms.CharField(max_length=50,help_text="事件")
	times = forms.DateTimeField(widget=forms.HiddenInput())
	class Meta:
		model = Shop_User
		fields = ('score',)

class DesireForm(forms.ModelForm):
	class Meta:
		model = Desire
		fields = ('consume',)
	
