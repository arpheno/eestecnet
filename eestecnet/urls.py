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

admin.autodiscover()
view = TemplateView.as_view(template_name='enet/index.html')
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eestecnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',view,{"target": "news"}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/$', ListView.as_view(model=Entry)),
    url(r'^news/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Entry)),
    url(r'^events/$', InternationalEvents.as_view(), name='events'),
    url(r'^events/(?P<pk>[-_\w]+)/$', EventDetail.as_view()),
    url(r'^events/(?P<pk>[-_\w]+)/apply/$', ApplyToEvent.as_view()),
    url(r'^cities/$', CommitmentList.as_view()),
    url(r'^cities/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Member)),
    url(r'^teams/$', TeamList.as_view()),
    url(r'^(?P<slug>[a-zA-Z0-9-_]+)/$', MemberDetail.as_view()),
    url(r'^login/', auth, name='login'),
    url(r'^logout/', out, name='logout'),
    url(r'^register/', new, name='register'),
    url(r'^people/(?P<slug>[\w.@+-]+)/$', EestecerProfile.as_view(), name='profile'),
    url(r'^teams/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Member)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':MEDIA_ROOT}),
    )
