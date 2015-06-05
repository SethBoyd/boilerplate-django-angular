from django.conf.urls import patterns, url
from demo.views import message_list

urlpatterns = patterns('',
    url(r'^/$', message_list)
)

