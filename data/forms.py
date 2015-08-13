from django import forms
from data.models import  Scenc,Area,Shop

class ScencForm(forms.ModelForm):
	class Meta:
		model = Scenc
		fields=('scenc_name',)

