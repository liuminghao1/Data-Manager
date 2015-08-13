from django.conf.urls import patterns,url

from data import views

urlpatterns = patterns('',
	url(r'^$',views.intime,name='data_intime'),
	url(r'^add/$',views.add,name='data_add'),
	url(r'^intime/$',views.intime,name='data_intime'),
	url(r'^check/$',views.check,name='data_check'),
	url(r'^add/(?P<add_name>\w+)$',views.add_data,name='data_add_data'),
)
