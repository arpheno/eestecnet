from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from wiki.views import WikiHome, PageDetail, PageCreate, PageUpdate, PageLatest, \
    PageRandom


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', login_required(WikiHome.as_view()), name='wikihome'),
    url(r'^create/?$', login_required(PageCreate.as_view()), name='createwikipage'),
    url(r'^random/?$', login_required(PageRandom.as_view()), name='randomwikipage'),
    url(r'^latest/?$', login_required(PageLatest.as_view()), name='latestwikipage'),
    url(r'^(?P<slug>[-\w]+)/?$', login_required(PageDetail.as_view()), name='wikipage'),
    url(r'^(?P<slug>[-\w]+)/update/?$', login_required(PageUpdate.as_view()),
        name='updatewikipage'),
)
