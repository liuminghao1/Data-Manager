from django.conf.urls import patterns,url

from shop import views

urlpatterns = patterns('',
	url(r'^tasks/$',views.tasks, name = 'shop_tasks'),
	url(r'^addtasks/$',views.addtasks, name = 'shop_addtasks'),
	url(r'^users/$',views.users, name = 'shop_users'),
	url(r'^add_score/$',views.add_score,name= 'add_score'),
)
