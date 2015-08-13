from django import forms

from book.models import Students


class testform(forms.ModelForm):
	
	class Meta:
		model = Students
		fields = ('name','phone',)
