from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
import account
from account.views import EestecerProfile,  EestecerUpdate, EestecerCreate, \
    Login, Logout, EestecerList
from eestecnet.settings import MEDIA_ROOT
from eestecnet.views import newsletter
from events.models import Event, Application
from events.views import EventDetail, ApplyToEvent, InternationalEvents, confirm_event, \
    FillInTransport
from materials.views import connector, index
from members.models import Member
from members.views import CommitmentList, TeamList, MemberDetail
from news.models import Entry

import random
from news.views import home

admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eestecnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',home.as_view(),name='home'),
    url(r'^news/$', ListView.as_view(model=Entry)),
    url(r'^about/$', home.as_view(),name='about'),
    url(r'^news/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Entry)),
    url(r'^events/$',  InternationalEvents.as_view(),  name='events',),
    url(r'^teams/$', TeamList.as_view(),name='teams'),
    url(r'^cities/$', CommitmentList.as_view(),name='cities'),
    url(r'^events/(?P<slug>[-\w]+)/$', EventDetail.as_view(), name='event'),
    url(r'^events/(?P<slug>[-\w]+)/apply$', ApplyToEvent.as_view(), name='eventapplication'),
    url(r'^events/(?P<slug>[-\w]+)/confirm/$', confirm_event, name='eventconfirmation'),
    url(r'^events/(?P<slug>[-\w]+)/transportation/$', FillInTransport.as_view(), name='eventtransportation'),
    url(r'^cities/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Member), name='city'),
    url(r'^teams/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Member), name='team'),
    url(r'^people/$', EestecerList.as_view(), name='people'),
    url(r'^people/me/$', EestecerUpdate.as_view(), name='userupdate'),
    url(r'^people/(?P<slug>[-\w]+)/$', EestecerProfile.as_view(), name='user'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^register/', EestecerCreate.as_view(), name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^materials/$', index, name='materials'),
    url(r'^newsletter/$', newsletter, name='newsletter'),
    url(r'^materials/connector/', connector, name='trtconnector'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':MEDIA_ROOT}),
    )
