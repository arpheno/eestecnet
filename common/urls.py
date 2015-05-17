from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

from apps.accounts.urls import grouprouter, group_participationrouter, membershiprouter
from apps.accounts.urls import group_accountrouter
from apps.accounts.urls import accountrouter
from apps.announcements.urls import announcementrouter
from apps.events.urls import eventrouter, package_router
from apps.prioritylists.urls import prioritylistrouter
from apps.questionnaires.urls import questionnairerouter
from apps.teams.urls import teamrouter
from common.routers import imagerouter
from settings.conf.media import MEDIA_ROOT


admin.autodiscover()
# App includes
urlpatterns = patterns(
    '',
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/', include(eventrouter.urls)),
    url(r'^api/', include(teamrouter.urls)),
    url(r'^api/', include(package_router.urls)),
    url(r'^api/', include(grouprouter.urls)),
    url(r'^api/', include(group_accountrouter.urls)),
    url(r'^api/', include(group_participationrouter.urls)),
    url(r'^api/', include(accountrouter.urls)),
    url(r'^api/', include(membershiprouter.urls)),
    url(r'^api/', include(questionnairerouter.urls)),
    url(r'^api/', include(prioritylistrouter.urls)),
    url(r'^api/', include(announcementrouter.urls)),
    url(r'^api/', include(imagerouter.urls)),
)
# Orphans
urlpatterns += patterns(
    '',
)
# Redirects
urlpatterns += patterns(
    '',
    url(r'seminar/?', RedirectView.as_view(url="http://www.crowdcast.io/eestec1")),
    url(r'congress/?', RedirectView.as_view(url="http://eestec.es")),
    url(r'ecm/?', RedirectView.as_view(url="http://ecm2014.com")),
    url(r'conference/?', RedirectView.as_view(url="http://conference.eestec.hu")),
    url(r'androidcompetition/?',
        RedirectView.as_view(url="https://competition.eestec.net")),
)
# If DEBUG is set, include the local file server
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT}),
    )
# Third party apps and pages


urlpatterns += patterns(
    '',
    url(r'^accounts_api/', include('registration_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^mail-queue/?$', include('mailqueue.urls')),
)
