from django.conf.urls import patterns,url

from bbs import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='bbs_index'),
	url(r'^publish/$',views.publish,name='bbs_publish'),
)
