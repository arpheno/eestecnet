"""Custom Map widget."""
from json import dumps
from urlparse import urljoin

from django.conf import settings
from django.forms.forms import Media
from django.forms.util import flatatt
from django.forms.widgets import Widget
from django.utils.html import escape
from django.utils.safestring import mark_safe

from gmapi import maps


JQUERY_URL = getattr(settings, 'GMAPI_JQUERY_URL',
                     'http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery'
                     '%s.js' % ('' if settings.DEBUG else '.min'))

MAPS_URL = getattr(settings, 'GMAPI_MAPS_URL',
                   'http://maps.google.com/maps/api/js?sensor=false')

# Same rules apply as ADMIN_MEDIA_PREFIX.
# Omit leading slash to make relative to MEDIA_URL.
MEDIA_PREFIX = getattr(settings, 'GMAPI_MEDIA_PREFIX', 'gmapi/')


class GoogleMap(Widget):
    def __init__(self, attrs=None):
        self.nojquery = (attrs or {}).pop('nojquery', False)
        self.nomapsjs = (attrs or {}).pop('nomapsjs', False)
        super(GoogleMap, self).__init__(attrs)

    def render(self, name, gmap, attrs=None):
        if gmap is None:
            gmap = maps.Map()
        default_attrs = {'id': name, 'class': 'gmap'}
        if attrs:
            default_attrs.update(attrs)
        final_attrs = self.build_attrs(default_attrs)
        width = final_attrs.pop('width', 500)
        height = final_attrs.pop('height', 400)
        style = (u'position:relative;width:%dpx;height:%dpx;' %
                 (width, height))
        final_attrs['style'] = style + final_attrs.get('style', '')
        map_div = (u'<div class="%s" style="position:absolute;'
                   u'width:%dpx;height:%dpx"></div>' %
                   (escape(dumps(gmap, separators=(',', ':'))),
                    width, height))
        map_img = (u'<img style="position:absolute;z-index:1" '
                   u'width="%(x)d" height="%(y)d" alt="Google Map" '
                   u'src="%(map)s&amp;size=%(x)dx%(y)d" />' %
                   {'map': escape(gmap), 'x': width, 'y': height})
        return mark_safe(u'<div%s>%s%s</div>' %
                         (flatatt(final_attrs), map_div, map_img))

    def _media(self):
        js = []
        if not self.nojquery:
            js.append(JQUERY_URL)
        if not self.nomapsjs:
            js.append(MAPS_URL)
        js.append(urljoin(MEDIA_PREFIX, 'js/jquery.gmapi%s.js' %
                          ('' if settings.DEBUG else '.min')))
        return Media(js=js)

    media = property(_media)
