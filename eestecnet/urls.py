from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView, TemplateView
from haystack.forms import SearchForm
from haystack.views import SearchView

from account.views import EestecerProfile, EestecerUpdate, EestecerCreate, \
    Login, Logout, EestecerList, complete
from eestecnet.settings import MEDIA_ROOT
from eestecnet.views import newsletter
from teams.views import CommitmentList, TeamList, Governance
from news.models import Entry
from news.views import home


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', home.as_view(), name='home'),
    url(r'^reset/', include('password_reset.urls')),
    url(r'^news/*$', ListView.as_view(model=Entry), name='news'),
    url(r'^androidcompetition/*$',
        TemplateView.as_view(template_name='android/home.html')),
    url(r'^conference/*$',
        TemplateView.as_view(template_name='conference/home.html')),
    url(r'^news/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Entry),
        name='news'),
    url(r'^events/*', include('events.urls')),
    url(r'^governance/*', Governance.as_view()),
    url(r'^teams/*$', TeamList.as_view(), name='teams'),
    url(r'^cities/*$', CommitmentList.as_view(), name='cities'),
    url(r'^cities/*', include('teams.urls', namespace="cities")),
    url(r'^teams/*', include('teams.urls', namespace="teams")),
    url(r'^people/*$', EestecerList.as_view(), name='people'),
    url(r'^people/me/*$', EestecerUpdate.as_view(), name='userupdate'),
    url(r'^people/(?P<slug>[-\w]+)/*$', EestecerProfile.as_view(),
        name='user'),
    url(r'^login/*', Login.as_view(), name='login'),
    url(r'^complete/(?P<ida>[-\w]+)/', complete, name='complete'),
    url(r'^logout/*', Logout.as_view(), name='logout'),
    url(r'^register/*', EestecerCreate.as_view(), name='register'),
    url(r'^admin/*', include(admin.site.urls)),
    url(r'^search/', SearchView(form_class=SearchForm)),
    url(r'^mail-queue/*$', include('mailqueue.urls')),
    url(r'^contact/*$', TemplateView.as_view(template_name='enet/contact.html')),
    url(r'^activities/*$', TemplateView.as_view(template_name='enet/activities.html')),
    url(r'^about/*$', TemplateView.as_view(template_name='enet/about.html')),
    url(r'^newsletter/*$', newsletter, name='newsletter'),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^materials/', include('elfinder.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'', include('pages.urls')),
)
