#-*- coding: utf-8 -*-
from django import forms
from bbs.models import Tba_user,Send_card,Follow_card
	

class Send_cardForm(forms.ModelForm):
	title = forms.CharField(max_length=28,help_text="标题")
	cardcontent = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','cols':'20'}),help_text="内容")
#	cardcontent = forms.CharField(widget=forms.Textarea,help_text="内容")
	class Meta:
		model = Send_card
		exclude =('tba_user',)

class UserForm(forms.ModelForm):
	
	class Meta:		
		fields =('username',)

