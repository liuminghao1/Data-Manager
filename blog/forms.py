from django import forms
from blog.models import  Blog,Message
import time
class BlogForm(forms.ModelForm):
	title = forms.CharField(max_length=128)
	update_time = forms.DateTimeField(widget=forms.HiddenInput())
	body = forms.CharField(max_length=128,help_text="please enter blog")
	class Meta:
		model = Blog
		fields=('title','body',)

class MessageForm(forms.ModelForm):
	author = forms.CharField(max_length=30,initial=' ',widget=forms.HiddenInput())
	update_time = forms.DateTimeField(widget=forms.HiddenInput(),initial=time.strftime('%Y-%m-%d %H:%M:%S'))
	body = forms.CharField(max_length=365)
	class Meta:
		model = Message
		fields=('body',)
