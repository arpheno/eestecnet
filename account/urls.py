from django.conf.urls import patterns, url
from django.views.generic import DetailView
from views import  auth, out, new, EestecerProfile

urlpatterns = patterns('',
                       url(r'^login/', auth, name='login'),
                       url(r'^logout/', out, name='logout'),
                       url(r'^register/', new, name='register'),
                       url(r'^id/(?P<pk>\d+)/$', EestecerProfile.as_view()),
                       url(r'^username/(?P<slug>[\w.@+-]+)/$', EestecerProfile.as_view()),

                       )
