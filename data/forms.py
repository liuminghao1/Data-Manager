#-*- coding:utf-8 -*-
from django import forms
from data.models import  Scenc,Area,Shop


attrs_dict = { 'class': 'required' } 

class ScencForm(forms.ModelForm):
	scenc_name = forms.CharField(max_length=120,help_text="场景名称",error_messages={'required': 'Please enter your name'})
	id = forms.CharField(widget=forms.HiddenInput(attrs={'value':'#'}))
	class Meta:
		model = Scenc
		fields=('scenc_name','id',)

class AreaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs): 
		super(AreaForm, self).__init__(*args, **kwargs)  
		scenc_choices = [(lang.scenc_name, lang.scenc_name) for lang in Scenc.objects.all()]
		self.fields['scenc'].choices = scenc_choices
#		self.fields['scenc'].choices = [('', '----------')] + [(lang.scenc_name, lang.scenc_name) for lang in Scenc.objects.all()]  
#	scenc = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES(attrs={'list-style':'none'}),help_text="所属场景")
	scenc = forms.ChoiceField(choices=(), widget=forms.Select(attrs=attrs_dict) ,help_text="所属场景")
	area_name = forms.CharField(max_length=120,help_text="区域名称")
	linkman =forms.CharField(max_length=120,help_text="负责人")
	phone =forms.CharField(max_length=120,help_text="电话")
	id = forms.CharField(widget=forms.HiddenInput(attrs={'value':'#'}))
	class Meta:
		model = Area
		fields=('area_name','linkman','phone','id')	
class ShopForm(forms.ModelForm):
	def __init__(self, *args, **kwargs): 
		super(ShopForm, self).__init__(*args, **kwargs) 
#	 	self.fields['scenc'].choices = scenc_choices  #初始化，增加scenc属性！
	 	area_choices = [(lang.area_name, lang.area_name) for lang in Area.objects.all()]
		self.fields['area'].choices = area_choices

#	scenc = forms.ChoiceField(choices=(), widget=forms.Select(attrs=attrs_dict) ,help_text="所属场景")
	area = forms.ChoiceField(choices=(), widget=forms.Select(attrs=attrs_dict) ,help_text="所属区域")	
	shop_name =forms.CharField(max_length=120,help_text="店铺名称")
	address =forms.CharField(max_length=120,help_text="店铺地址")
	number =forms.CharField(max_length=120,help_text="店号")
	remake =forms.CharField(max_length=120,help_text="备注")
	linkman =forms.CharField(max_length=120,help_text="负责人")
	phone =forms.CharField(max_length=120,help_text="电话")
	id = forms.CharField(widget=forms.HiddenInput(attrs={'value':'#'}))
	class Meta:
		model = Shop
		fields =('shop_name','address','number','remake','linkman','phone','id')
