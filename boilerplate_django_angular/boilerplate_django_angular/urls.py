from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boilerplate_django_angular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/demo', include('demo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
