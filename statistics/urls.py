from django.conf.urls import patterns, url
from django.contrib import admin

from statistics.views import simpleStatistics


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/*$', simpleStatistics, name='statistics')
)
