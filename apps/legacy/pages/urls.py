from django.conf.urls import patterns, url
from django.contrib import admin

from apps.pages.views import StaticPage, StaticPageEdit, NewWebsiteFeedback


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'eestecnet.views.home', name='home'),
                       url(r'^pages/feedback/?$', NewWebsiteFeedback.as_view(),
                           name='website-feedback'),
                       url(r'^edit/(?P<url>[-_/\w]+)', StaticPageEdit.as_view()),
                       url(r'^(?P<url>[-_/\w]+)', StaticPage.as_view()),
                       )
