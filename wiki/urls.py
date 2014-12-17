from django.conf.urls import patterns, url
from django.contrib import admin

from wiki.views import WikiHome, PageDetail, PageCreate, PageUpdate


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/*$', WikiHome.as_view(), name='wikihome'),
    url(r'^create/*/*$', PageCreate.as_view(), name='createwikipage'),
    url(r'^(?P<slug>[-\w]+)/*$', PageDetail.as_view(), name='wikipage'),
    url(r'^(?P<slug>[-\w]+)/update/*$', PageUpdate.as_view(), name='updatewikipage'),
)
