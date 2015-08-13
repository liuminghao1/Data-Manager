from django.shortcuts import render

from data.models import Scenc,Area,Shop

from data.forms import ScencForm
# Create your views here.

def index(request):
	return render(request,"data/index.html",{})
def add(request):
	scencs = Scenc.objects.all()
	return render(request,"data/add.html",{'scencs':scencs})
	
def intime(request):
	return render(request,"data/intime.html",{})

def check(request):
	return render(request,"data/check.html",{})

def add_data(request,add_name):
	forms = {}
	if add_name == 'scenc':
		if request.method == 'POST':
			form = ScencForm(request.POST)
			if form.is_valid():
				form.save(commit=True)
				return render(request,"data/add.html",{})
		form = ScencForm()	
		return render(request,"data/add_scenc.html",{'form': form})
