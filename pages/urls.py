from django.conf.urls import patterns, url
from django.contrib import admin

from pages.views import StaticPage


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'eestecnet.views.home', name='home'),
                       url(r'^(?P<url>[-_/\w]+)', StaticPage.as_view()),
)
