from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from events.models import Event, Application
from events.views import EventList, EventDetail, ApplyToEvent
from members.views import CommitmentList, TeamList
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
    url(r'^events/$', ListView.as_view(model=Event)),
    url(r'^events/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Event)),
    url(r'^events/(?P<pk>[-_\w]+)/apply/$', ApplyToEvent.as_view()),
    url(r'^cities/$', CommitmentList.as_view()),
    url(r'^teams/$', TeamList.as_view()),
    url(r'^members/$', ListView.as_view(model=Event)),
    url(r'^members/(?P<pk>[-_\w]+)/$', DetailView.as_view(model=Event)),

    )
