#-*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
	us = forms.CharField(label=u'用户名',max_length=100,widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'用户名', 'required': '', 'autofocus': '','id':'us'}
        ),
    )
	pwd = forms.CharField(label=u'密码',widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': u'密码', 'required': '','id':'pwd'}
        )
    )
