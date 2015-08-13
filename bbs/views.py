from django.shortcuts import render
from bbs.forms import Send_cardForm
from bbs.models import Tba_user,Send_card
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

def index(request):
	cards = Send_card.objects.order_by('-date')
	print request.session.items()
	return render(request,'bbs/index.html',{'cards':cards})


def publish(request):

	if request.method == 'POST':
		form =  Send_cardForm(request.POST)
		if form.is_valid() and request.user.is_authenticated():

			U = User.objects.get(username=request.user)
			try:
				U_table = Tba_user.objects.get(user=U)
			except Tba_user.DoesNotExist:
				U_table = Tba_user(user=U)
				U_table.save()
			cred = form.save(commit=False)
			cred.tba_user = U_table
			cred.save()
			return render(request,'bbs/publish.html',{'id':request.POST})
	else:
		form =  Send_cardForm()	

	return render(request,'bbs/publish.html',{'form':form})
