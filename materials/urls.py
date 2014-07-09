from django.conf.urls import patterns, url
from materials.views import connector, index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^connector/$', connector, name="trtconnector"),
)
