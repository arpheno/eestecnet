"""URL pattern for serving static media. Use only to DEBUG!

Add something like the following to the bottom of your urls.py:

from django.conf import settings
if settings.DEBUG:
    urlpatterns = patterns('',
        (r'', include('gmapi.urls.media')),
    ) + urlpatterns
"""
from os import path
from urlparse import urljoin

from django.conf import settings

from django.conf.urls.defaults import *



# Same rules apply as regular MEDIA_ROOT.
MEDIA_ROOT = getattr(settings, 'GMAPI_MEDIA_ROOT',
                     path.abspath(path.join(path.dirname(
                         path.dirname(__file__)), 'media', 'gmapi')))

# Same rules apply as ADMIN_MEDIA_PREFIX.
# Omit leading slash to make relative to MEDIA_URL.
MEDIA_PREFIX = getattr(settings, 'GMAPI_MEDIA_PREFIX', 'gmapi/')

if MEDIA_PREFIX.startswith('http://') or MEDIA_PREFIX.startswith('https://'):
    urlpatterns = []
else:
    urlpatterns = patterns('',
                           (r'^%s(?P<path>.*)$' %
                            urljoin(settings.MEDIA_URL, MEDIA_PREFIX).lstrip('/'),
                            'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
