from django.conf.urls import patterns,url

from test1 import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='test1_index'),
)
