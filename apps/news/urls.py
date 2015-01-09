from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import DetailView

from apps.news.models import Entry
from apps.news.views import NewsList


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', NewsList.as_view(), name='news'),
    url(r'^/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Entry), name='news'),
)
