#-*- coding:utf-8 -*-
from django.shortcuts import render

from data.models import Scenc,Area,Shop

from data.forms import ScencForm,AreaForm,ShopForm
# Create your views here.

def index(request):
	return render(request,"data/index.html",{})
def status_data(request,status_name):
	forms ={}
	forms['status_name'] = status_name
	if status_name =='scenc':
		forms['scencs'] = Scenc.objects.all()
		return render(request,"data/status_scenc.html",forms)
	elif status_name =='area':
		forms['areas'] = Area.objects.all()
		return render(request,"data/status_area.html",forms)
	elif status_name =='shop':
		forms['scencs'] = Scenc.objects.all()
		forms['areas'] = Area.objects.all()
		forms['shops'] = Shop.objects.all()
		return render(request,"data/status_shop.html",forms)
	
def intime(request):
	return render(request,"data/intime.html",{})

def check(request):
	return render(request,"data/check.html",{})

def change(request,change_name,class_id):
	forms ={}
	forms['change_name'] = change_name
	if change_name == 'scenc':
		scenc = Scenc.objects.get(id=class_id)
		forms['form'] = ScencForm(instance=scenc)
		return render(request,"data/add_scenc.html",forms)
	elif change_name == 'area':
		area=Area.objects.get(id=class_id)
		forms['form']  = AreaForm(instance=area) 
		return render(request,"data/add_area.html",forms)
	elif change_name == 'shop':
		shop=Shop.objects.get(id=class_id)
		forms['form'] = ShopForm(instance=shop)
		return render(request,"data/add_shop.html",forms)
def delete(request,delete_name,delete_id):
	if delete_name == 'scenc':
		Scenc.objects.get(id=delete_id).delete()
		return check(request)
		
	elif delete_name == 'area':
		Area.objects.get(id=delete_id).delete()
		return check(request)

	elif delete_name == 'shop':
		Shop.objects.get(id=delete_id).delete()
		return check(request)

def add_data(request,add_name):
	forms = {}
	forms['add_name'] = add_name
	if add_name == 'scenc':
		if request.method == 'POST':
			form = ScencForm(request.POST)
			if form.is_valid():
				try:
					scenc = Scenc.objects.get(id = form.cleaned_data['id'])
				except :
					form.save(commit=True)
					return check(request)
				scenc.scenc_name = form.cleaned_data['scenc_name']
				scenc.save()
				return check(request)
		forms['form'] = ScencForm()
		
		return render(request,"data/add_scenc.html",forms)
	elif add_name == 'area':
		if request.method == 'POST':
			form = AreaForm(request.POST)
			if form.is_valid():
				try:  
					area = Area.objects.get(id = form.cleaned_data['id'])
				except :
					f = form.save(commit=False)
					s = Scenc.objects.get(scenc_name = form.cleaned_data['scenc']) #获取下拉框的值
					f.scenc = s
					f.save()
					return check(request)
				s = Scenc.objects.get(scenc_name = form.cleaned_data['scenc'])
				area.scenc = s
				area.linkman = form.cleaned_data['linkman']
				area.phone=form.cleaned_data['phone']
				area.area_name = form.cleaned_data['area_name']
				area.save()
				return check(request)				

		forms['form']  = AreaForm()	
		return render(request,"data/add_area.html",forms)
	elif add_name == 'shop':
		if request.method == 'POST':
			form = ShopForm(request.POST)
			if form.is_valid():
				try:
					shop = Shop.objects.get(id = form.cleaned_data['id'])
				except:
					f = form.save(commit=False)
					f.area = Area.objects.get(area_name = form.cleaned_data['area'])
					f.save()
					return check(request)
				
				shop.area= Area.objects.get(area_name = form.cleaned_data['area'])
				shop.shop_name=form.cleaned_data['shop_name']
				shop.address=form.cleaned_data['address']
				shop.number=form.cleaned_data['number']
				shop.remake=form.cleaned_data['remake']
				shop.linkman=form.cleaned_data['linkman']
				shop.phone=form.cleaned_data['phone']
				shop.save()
				return check(request)
		forms['form'] = ShopForm()
		return render(request,"data/add_shop.html",forms)
#def status(request):
	
