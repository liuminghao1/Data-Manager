from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^accounts/', include('registration.backends.simple.urls')),	
    url(r'^test1/$',include('test1.urls')),
    url(r'^bbs/',include('bbs.urls')),
    url(r'^rebbs/',include('rebbs.urls')),
    url(r'^data/',include('data.urls')),
)

