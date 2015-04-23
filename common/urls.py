from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

from settings.conf.media import MEDIA_ROOT


admin.autodiscover()
# App includes
urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
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
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^mail-queue/?$', include('mailqueue.urls')),
)
