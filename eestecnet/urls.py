from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, RedirectView, TemplateView
from haystack.forms import SearchForm
from haystack.views import SearchView

from apps.account.views import EestecerCreate, \
    Login, Logout, complete, MassCommunication, PrivilegedCommunication
from eestecnet.settings.basic import MEDIA_ROOT
from eestecnet.views import newsletter
from apps.pages.models import Stub
from apps.pages.views import ActivityStubs, AboutStubs
from apps.teams.views import CommitmentList, TeamList, Governance
from apps.news.views import home


admin.autodiscover()
# App includes
urlpatterns = patterns(
    '',
    url(r'^$', home.as_view(), name='home'),
    url(r'^teams/?$', TeamList.as_view(), name='teams'),
    url(r'^cities/?$', CommitmentList.as_view(), name='cities'),
    url(r'^cities/angular/?$',
        TemplateView.as_view(template_name="teams/angular/teams_list.html")),
    url(r'^cities', include('apps.teams.urls', namespace="cities",app_name="cities")),
    url(r'^teams', include('apps.teams.urls', namespace="teams",app_name="teams")),
    url(r'^events', include('apps.events.urls')),
    url(r'^people', include('apps.account.urls')),
    url(r'^materials', include('apps.elfinder.urls')),
    url(r'^news', include('apps.news.urls')),
    url(r'^wiki/', include('apps.wiki.urls')),
    url(r'^statistics', include('apps.statistics.urls')),  # not currently used
)
# Orphans
urlpatterns += patterns(
    '',
    url(r'^login/?', Login.as_view(), name='login'),
    url(r'^complete/(?P<ida>[-\w]+)/?$', complete, name='complete'),
    url(r'^logout/?', Logout.as_view(), name='logout'),
    url(r'^register/?', EestecerCreate.as_view(), name='register'),
    url(r'^search/', SearchView(form_class=SearchForm)),
    url(r'^activities/?$', ActivityStubs.as_view(), name='activities'),
    url(r'^sitemap/?$', ListView.as_view(model=Stub), name='sitemap'),
    url(r'^about/?$', AboutStubs.as_view(), name='about'),
    url(r'^newsletter/?$', newsletter, name='newsletter'),
    url(r'^active/?$', MassCommunication.as_view(), name='masscommunication'),
    url(r'^privileged/?$', PrivilegedCommunication.as_view(), name='privcommunication'),
    url(r'^governance/?$', Governance.as_view(), name='governance'),
)
# Redirects
urlpatterns += patterns(
    '',
    url(r'seminar/?', RedirectView.as_view(url="http://www.crowdcast.io/eestec1")),
    url(r'congress/?', RedirectView.as_view(url="http://eestec.es")),
    url(r'ecm/?', RedirectView.as_view(url="http://ecm2014.com")),
    url(r'conference/?', RedirectView.as_view(url="http://conference.eestec.hu")),
)
# If DEBUG is set, include the local file server
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT}),
    )
#Third party apps and pages
urlpatterns += patterns(
    '',
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^mail-queue/?$', include('mailqueue.urls')),
    url(r'^reset/', include('apps.password_reset.urls')),
    url(r'', include('apps.pages.urls')),
)
