from django.conf.urls import patterns,url

from rebbs import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='rebbs_index'),
	url(r'login',views.usLogin,name='rebbs_login'),
)
