from django.conf.urls import patterns,url

from blog import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^category/(?P<category_name>[\w\-]+)/$',views.category_page,name='category'),
	url(r'list/$',views.list,name='list'),
	url(r'article/(?P<article_num>[\d]+)/$',views.article,name='article'),
	url(r'^add_blog/',views.add_blog,name='add_blog'),
	url(r'^message/$',views.message,name="messwge"),
)
