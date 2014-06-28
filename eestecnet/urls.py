from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
import account
from account.views import EestecerProfile, auth, out, new
from eestecnet.settings import MEDIA_ROOT
from events.models import Event, Application
from events.views import EventDetail, ApplyToEvent, InternationalEvents
from members.models import Member
from members.views import CommitmentList, TeamList, MemberDetail
from news.models import Entry

import random
admin.autodiscover()
view = TemplateView.as_view(template_name='enet/index.html',)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eestecnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',view),
    url(r'^news/$', ListView.as_view(model=Entry)),
    url(r'^news/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Entry)),
    url(r'^events/$',  InternationalEvents.as_view(),  name='events',),
    url(r'^teams/$', TeamList.as_view(),name='teams'),
    url(r'^cities/$', CommitmentList.as_view(),name='cities'),
    url(r'^events/(?P<slug>[-\w]+)/$', EventDetail.as_view(), name='event'),
    url(r'^events/(?P<slug>[-\w]+)/apply$', ApplyToEvent.as_view(), name='eventapplication'),
    url(r'^cities/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Member), name='member'),
    url(r'^teams/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Member), name='member'),
    url(r'^people/(?P<slug>[-\w]+)/$', EestecerProfile.as_view(), name='user'),
    url(r'^login/', auth, name='login'),
    url(r'^logout/', out, name='logout'),
    url(r'^register/', new, name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':MEDIA_ROOT}),
    url(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/home.html',)),
    url(r'^bootstrap/events/$',TemplateView.as_view(template_name='bootstrap/events.html',), name='bootstrap-events'),
    )
