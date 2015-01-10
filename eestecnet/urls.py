from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, TemplateView, RedirectView
from haystack.forms import SearchForm
from haystack.views import SearchView

from account.views import EestecerProfile, EestecerUpdate, EestecerCreate, \
    Login, Logout, EestecerList, complete, TrainingList, MassCommunication
from eestecnet.settings import MEDIA_ROOT
from eestecnet.views import newsletter
from events.views import InternationalEvents
from pages.models import Stub
from pages.views import ActivityStubs, AboutStubs, Documents
from teams.views import CommitmentList, TeamList, Governance, History
from news.views import home, NewsList


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', home.as_view(), name='home'),
    url(r'^reset/', include('password_reset.urls')),
    url(r'^news/?$', NewsList.as_view(), name='news'),
    url(r'^news/', include('news.urls')),
    url(r'^androidcompetition/?$',
        TemplateView.as_view(template_name='android/home.html'), name="competition"),
    url(r'^conference/?$',
        TemplateView.as_view(template_name='conference/home.html'),
        name='conference'),
    url(r'^events/?$', InternationalEvents.as_view(), name='events'),
    url(r'^events/', include('events.urls')),
    url(r'^governance/?$', Governance.as_view(), name='governance'),
    url(r'^documents/?$', Documents.as_view(), name='documents'),
    url(r'^sitemap/?$', ListView.as_view(model=Stub), name='sitemap'),
    url(r'^teams/?$', TeamList.as_view(), name='teams'),
    url(r'^cities/?$', CommitmentList.as_view(), name='cities'),
    url(r'^cities/', include('teams.urls', namespace="cities")),
    url(r'^teams/', include('teams.urls', namespace="teams")),
    url(r'^people/?$', EestecerList.as_view(), name='people'),
    url(r'^people/me/?$', EestecerUpdate.as_view(), name='userupdate'),
    url(r'^people/(?P<slug>[-\w]+)/?$', EestecerProfile.as_view(),
        name='user'),
    url(r'^people/(?P<slug>[-\w]+)/certificate/?$', TrainingList.as_view(),
        name='certificate'),
    url(r'^login/?', Login.as_view(), name='login'),
    url(r'^complete/(?P<ida>[-\w]+)/?$', complete, name='complete'),
    url(r'^logout/?', Logout.as_view(), name='logout'),
    url(r'^register/?', EestecerCreate.as_view(), name='register'),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^search/', SearchView(form_class=SearchForm)),
    url(r'^mail-queue/?$', include('mailqueue.urls')),
    url(r'^contact/?$', TemplateView.as_view(template_name='enet/contact.html')),
    url(r'^activities/?$', ActivityStubs.as_view(), name='activities'),
    url(r'^about/?$', AboutStubs.as_view(), name='about'),
    url(r'^newsletter/?$', newsletter, name='newsletter'),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^materials', include('elfinder.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^history/?$', History.as_view(), name="history"),
    url(r'^statistics/', include('statistics.urls')),
    url(r'^wiki/', include('wiki.urls')),
    url(r'^active/?$', MassCommunication.as_view(), name='masscommunication'),
    url(r'^seminar/?', RedirectView.as_view(url="http://www.crowdcast.io/e/eestec1")),
    url(r'', include('pages.urls')),
)
