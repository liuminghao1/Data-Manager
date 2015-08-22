from django.conf.urls import patterns,url

from data import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='data_index'),
	url(r'^status/(?P<status_name>\w+)$',views.status_data,name='data_status'),
	url(r'^intime/$',views.intime,name='data_intime'),
	url(r'^intime/(?P<intime_id>\d+)/$',views.intime,name='data_intime_id'),
	url(r'^check/$',views.check,name='data_check'),
	url(r'^check/(?P<check_name>\w+)$',views.check,name='data_check_area'),
	url(r'^add/(?P<add_name>\w+)$',views.add_data,name='data_add_data'),
	url(r'^(?P<change_name>\w+)/(?P<class_id>\d+)/$',views.change,name='data_change'),
	url(r'^delete/(?P<delete_name>\w+)/(?P<delete_id>\d+)/$',views.delete,name='data_delete'),
)
