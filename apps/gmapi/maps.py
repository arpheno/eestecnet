"""Implements the Google Maps API v3."""
import time
import urllib
from json import loads

from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import force_unicode, smart_str

from apps.gmapi.utils.http import urlencode


STATIC_URL = getattr(settings, 'GMAPI_STATIC_URL',
                     'http://maps.google.com/maps/api/staticmap')

GEOCODE_URL = getattr(settings, 'GMAPI_GEOCODE_URL',
                      'http://maps.google.com/maps/api/geocode')

CHART_URL = getattr(settings, 'GMAPI_CHART_URL',
                    'http://chart.apis.google.com/chart')


class MapClass(dict):
    """A base class for Google Maps API classes."""
    _getopts = {}
    _setopts = {}

    def __getattr__(self, item):
        """Handle generic get and set option methods."""
        if 'arg' in self:
            if item in self._getopts:
                key = self._getopts[item]

                def func():
                    return self['arg'].get('opts', {}).get(key)

                return func
            if item in self._setopts:
                key = self._setopts[item]

                def func(value):
                    # Call setOptions so that it can be overridden.
                    self.setOptions({key: value})

                return func
        raise AttributeError, item

    def __str__(self):
        """Handle string conversion."""
        if hasattr(self, '__unicode__'):
            return force_unicode(self).encode('utf-8')
        return '%s object' % self.__class__.__name__

    def setOptions(self, opts):
        if 'arg' in self and opts:
            self['arg'].setdefault('opts', {}).update(opts)


class MapConstant(MapClass):
    """A custom constant class.

    For holding special Google Maps constants. When parsed by
    JSONEncoder and subsequently by our custom jQuery plugin,
    it will be converted to the actual constant value.

    """

    def __init__(self, cls, const):
        super(MapConstant, self).__init__(val='%s.%s' % (cls, const))
        self.const = const

    def __setitem__(self, key, value):
        raise KeyError, key

    def __unicode__(self):
        return self.const.lower()


class MapConstantClass(object):
    """A custom factory class for constants."""

    def __init__(self, name, constants):
        for const in constants:
            setattr(self, const, MapConstant(name, const))


class Map(MapClass):
    """A Google Map.

    Equivalent to google.maps.Map. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Map instance.

    """
    _getopts = {
        'getCenter': 'center',
        'getMapTypeId': 'mapTypeId',
        'getZoom': 'zoom',
    }
    _setopts = {
        'setCenter': 'center',
        'setMapTypeId': 'mapTypeId',
        'setZoom': 'zoom',
    }

    def __init__(self, opts=None):
        """mapDiv is not used, so not included in parameters."""
        super(Map, self).__init__(cls='Map')
        self['arg'] = Args(['mapDiv', 'opts'], ['div'])
        self.setOptions(opts)

    def __unicode__(self):
        """Produces a static map image url.

        Don't forget to set the map option 'size' (as an instance
        of maps.Size). Or alternatively you can append it to the
        resulting string (e.g. '&size=400x400').

        """
        opts = self['arg'].get('opts', {})
        params = []
        for p in ['center', 'zoom', 'size', 'format', 'language']:
            if p in opts:
                params.append((p, unicode(opts[p])))
        if 'mapTypeId' in opts:
            params.append(('maptype', unicode(opts['mapTypeId'])))
        if 'visible' in opts:
            params.append(('visible', '|'.join([unicode(v)
                                                for v in opts['visible']])))
        if 'mkr' in self:
            params.append(('markers', [unicode(m) for m in self['mkr']]))
        if 'pln' in self:
            params.append(('path', [unicode(p) for p in self['pln']]))
        if 'pgn' in self:
            params.append(('path', [q for p in self['pgn']
                                    for q in unicode(p).split('&path=')]))
        params.append(('sensor', 'true' if opts.get('sensor') else 'false'))
        return '%s?%s' % (STATIC_URL, urlencode(params, doseq=True))

    def _markers(self):
        return self.get('mkr', [])

    markers = property(_markers)

    def _polylines(self):
        return self.get('pln', [])

    polylines = property(_polylines)

    def _polygons(self):
        return self.get('pgn', [])

    polygons = property(_polygons)


MapTypeId = MapConstantClass('MapTypeId',
                             ('HYBRID', 'ROADMAP', 'SATELLITE', 'TERRAIN',))

MapTypeControlStyle = MapConstantClass('MapTypeControlStyle',
                                       ('DEFAULT', 'DROPDOWN_MENU',
                                        'HORIZONTAL_BAR',))

NavigationControlStyle = MapConstantClass('NavigationControlStyle',
                                          ('ANDROID', 'DEFAULT', 'SMALL',
                                           'ZOOM_PAN',))

ScaleControlStyle = MapConstantClass('ScaleControlStyle', ('DEFAULT',))

ControlPosition = MapConstantClass('ControlPosition',
                                   ('BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT',
                                    'LEFT', 'RIGHT', 'TOP', 'TOP_LEFT',
                                    'TOP_RIGHT',))


class Marker(MapClass):
    """A Google Marker.

    Equivalent to google.maps.Marker. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Marker instance.

    """
    _getopts = {
        'getClickable': 'clickable',
        'getCursor': 'cursor',
        'getDraggable': 'draggable',
        'getFlat': 'flat',
        'getIcon': 'icon',
        'getPosition': 'position',
        'getShadow': 'shadow',
        'getShape': 'shape',
        'getTitle': 'title',
        'getVisible': 'visible',
        'getZIndex': 'zIndex',
    }
    _setopts = {
        'setClickable': 'clickable',
        'setCursor': 'cursor',
        'setDraggable': 'draggable',
        'setFlat': 'flat',
        'setIcon': 'icon',
        'setMap': 'map',
        'setPosition': 'position',
        'setShadow': 'shadow',
        'setShape': 'shape',
        'setTitle': 'title',
        'setVisible': 'visible',
        'setZIndex': 'zIndex',
    }

    def __init__(self, opts=None):
        super(Marker, self).__init__(cls='Marker')
        self._map = None
        self._size = None
        self._color = None
        self._label = None
        self['arg'] = Args(['opts'])
        self.setOptions(opts)

    def __unicode__(self):
        opts = self['arg'].get('opts', {})
        params = []
        if self._size:
            params.append('size:%s' % self._size)
        if self._color or self._label:
            if self._color:
                params.append('color:%s' % self._color)
            if self._label:
                params.append('label:%s' % self._label)
        elif 'icon' in opts:
            params.append('icon:%s' % opts['icon'])
            if 'shadow' in opts:
                params.append('shadow:%s' %
                              'true' if opts['shadow'] else 'false')
        if 'position' in opts:
            params.append(unicode(opts['position']))
        return '|'.join(params)

    def getMap(self):
        return self._map

    def setOptions(self, options):
        if options and 'map' in options:
            if self._map:
                # Remove this marker from the map.
                self._map['mkr'].remove(self)
            # Save new map reference.
            self._map = options.pop('map')
            if self._map:
                # Add this marker to the map.
                self._map.setdefault('mkr', []).append(self)
        if options:
            self._size = options.pop('size', self._size)
            self._color = options.pop('color', self._color)
            self._label = options.pop('label', self._label)
            if (self._color or self._label) and 'icon' not in options:
                l = self._label or u'\u2022'
                c = (self._color or 'FF776B').lstrip('0x')
                options['icon'] = MarkerImage('%s?chst=d_map_pin_letter'
                                              '&chld=%s|%s' % (CHART_URL, l, c),
                                              anchor=Point(10, 33))
                options['shadow'] = MarkerImage('%s?chst=d_map_pin_shadow' %
                                                CHART_URL, anchor=Point(12, 35))
            elif 'icon' in options:
                self._color = None
                self._label = None
        super(Marker, self).setOptions(options)


class MarkerImage(MapClass):
    """An image to be used as the icon or shadow for a Marker.

    Equivalent to google.maps.MarkerImage. When parsed by
    JSONEncoder and subsequently by our custom jQuery plugin,
    it will be converted to an actual google.maps.MarkerImage
    instance.

    """

    def __init__(self, url, size=None, origin=None, anchor=None,
                 scaledSize=None):
        super(MarkerImage, self).__init__(cls='MarkerImage')
        self['arg'] = Args(['url', 'size', 'origin', 'anchor', 'scaledSize'],
                           [url])
        if size:
            self['arg'].setdefault('size', size)
        if origin:
            self['arg'].setdefault('origin', origin)
        if anchor:
            self['arg'].setdefault('anchor', anchor)
        if scaledSize:
            self['arg'].setdefault('scaledSize', scaledSize)

    def __unicode__(self):
        return self['arg'].get('url')


class Polyline(MapClass):
    """A Google Polyline.

    Equivalent to google.maps.Polyline. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Polyline instance.

    """
    _getopts = {
        'getPath': 'path',
    }
    _setopts = {
        'setMap': 'map',
        'setPath': 'path',
    }

    def __init__(self, opts=None):
        super(Polyline, self).__init__(cls='Polyline')
        self._map = None
        self['arg'] = Args(['opts'])
        self.setOptions(opts)

    def __unicode__(self):
        opts = self['arg'].get('opts', {})
        params = []
        if 'strokeColor' in opts:
            color = 'color:0x%s' % opts['strokeColor'].lstrip('#').lower()
            if 'strokeOpacity' in opts:
                color += '%02x' % min(max(opts['strokeOpacity'] * 255, 0), 255)
            params.append(color)
        if 'strokeWeight' in opts:
            params.append('weight:%d' % opts['strokeWeight'])
        if 'path' in opts:
            params.append('|'.join([unicode(p) for p in opts['path']]))
        return '|'.join(params)

    def getMap(self):
        return self._map

    def setOptions(self, options):
        if options and 'map' in options:
            if self._map:
                # Remove this polyline from the map.
                self._map['pln'].remove(self)
            # Save new map reference.
            self._map = options.pop('map')
            if self._map:
                # Add this polyline to the map.
                self._map.setdefault('pln', []).append(self)
        super(Polyline, self).setOptions(options)


class Polygon(MapClass):
    """A Google Polygon.

    Equivalent to google.maps.Polygon. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Polygon instance.

    """
    _getopts = {
        'getPaths': 'paths',
    }
    _setopts = {
        'setMap': 'map',
        'setPaths': 'paths',
    }

    def __init__(self, opts=None):
        super(Polygon, self).__init__(cls='Polygon')
        self._map = None
        self['arg'] = Args(['opts'])
        self.setOptions(opts)

    def __unicode__(self):
        opts = self['arg'].get('opts', {})
        params = []
        paths = []
        if 'fillColor' in opts:
            fillcolor = ('fillcolor:0x%s' %
                         opts['fillColor'].lstrip('#').lower())
            if 'fillOpacity' in opts:
                fillcolor += ('%02x' %
                              min(max(opts['fillOpacity'] * 255, 0), 255))
            params.append(fillcolor)
        if 'strokeColor' in opts:
            color = 'color:0x%s' % opts['strokeColor'].lstrip('#').lower()
            if 'strokeOpacity' in opts:
                color += '%02x' % min(max(opts['strokeOpacity'] * 255, 0), 255)
            params.append(color)
        if 'strokeWeight' in opts:
            params.append('weight:%d' % opts['strokeWeight'])
        if 'paths' in opts:
            for path in opts['paths']:
                loop = ['' if path[-1].equals(path[0]) else unicode(path[0])]
                paths.append('|'.join(params + [unicode(p) for p in path] +
                                      loop))
        return '&path='.join(paths)

    def getMap(self):
        return self._map

    def getPath(self):
        return (self.getPaths() or [None])[0]

    def setOptions(self, options):
        if options and 'map' in options:
            if self._map:
                # Remove this polygon from the map.
                self._map['pgn'].remove(self)
            # Save new map reference.
            self._map = options.pop('map')
            if self._map:
                # Add this polygon to the map.
                self._map.setdefault('pgn', []).append(self)
        super(Polygon, self).setOptions(options)

    def setPath(self, path):
        self.setPaths([path])


class InfoWindow(MapClass):
    """A Google InfoWindow.

    Equivalent to google.maps.InfoWindow. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.InfoWindow instance.

    """
    _getopts = {
        'getContent': 'content',
        'getPosition': 'position',
        'getZIndex': 'zIndex',
    }
    _setopts = {
        'setContent': 'content',
        'setPosition': 'position',
        'setZIndex': 'zIndex',
    }

    def __init__(self, opts=None):
        super(InfoWindow, self).__init__(cls='InfoWindow')
        self['arg'] = Args(['opts'])
        self.setOptions(opts)

    def open(self, map, anchor=None):
        """Link this InfoWindow to a Marker and/or Map."""
        if anchor:
            # Make sure the marker is assigned to the specified map.
            anchor.setMap(map)
            anchor['nfo'] = self
        else:
            map['nfo'] = self


class Geocoder(object):
    """A service for converting between an address and a LatLng.

    This is equivalent to using google.maps.Geocoder except that
    it makes use of the Web Service. You should always use the
    javascript API version in preference to this one as query
    limits are per IP. The javascript API uses the client's IP
    and thus is much less likely to hit any limits.

    """
    # Handle blocking and sleeping at class level.
    _block = False
    _sleep = 0
    _last = 0

    def geocode(self, request, callback=None):
        """Geocode a request.

        Unlike the javascript API, this method is blocking. So, even
        though a callback function is supported, the method will also
        return the results and status directly.

        """
        # Handle any unicode in the request.
        if 'address' in request:
            request['address'] = smart_str(request['address'],
                                           strings_only=True).lower()
        # Add the sensor parameter if needed.
        if 'sensor' in request:
            if request['sensor'] != 'false':
                request['sensor'] = 'true' if request['sensor'] else 'false'
        else:
            request['sensor'] = 'false'
        cache_key = urlencode(request)
        url = '%s/json?%s' % (GEOCODE_URL, cache_key)
        # Try up to 30 times if over query limit.
        for _ in xrange(30):
            # Check if result is already cached.
            data = cache.get(cache_key)
            if data is None:
                if (max(0, time.time() - self.__class__._last) <
                        self.__class__._sleep):
                    # Wait a bit so that we don't make requests too fast.
                    time.sleep(max(0, self.__class__._sleep +
                                   self.__class__._last - time.time()))
                data = urllib.urlopen(url).read()
                self.__class__._last = time.time()
            response = loads(data)
            status = response['status']

            if status == 'OVER_QUERY_LIMIT':
                # Over limit, increase delay a bit.
                if self.__class__._block:
                    break
                self.__class__._sleep += .1
            else:
                # Save results to cache.
                cache.set(cache_key, data)
                if status == 'OK':
                    # Successful query, clear block if there is one.
                    if self.__class__._block:
                        self.__class__._block = False
                        self.__class__._sleep = 0
                    results = _parseGeocoderResult(response['results'])
                    if callback:
                        callback(results, status)
                    return results, status
                else:
                    return None, status
        self.__class__._block = True
        raise SystemError('Geocoding has failed too many times. '
                          'You might have exceeded your daily limit.')


def _parseGeocoderResult(result):
    """ Parse Geocoder Results.

    Traverses the results converting any latitude-longitude pairs
    into instances of LatLng and any SouthWest-NorthEast pairs
    into instances of LatLngBounds.

    """
    # Check for LatLng objects and convert.
    if (isinstance(result, dict) and 'lat' in result and 'lng' in result):
        result = LatLng(result['lat'], result['lng'])
    # Continue traversing.
    elif isinstance(result, dict):
        for item in result:
            result[item] = _parseGeocoderResult(result[item])
        # Check for LatLngBounds objects and convert.
        if ('southwest' in result and 'northeast' in result):
            result = LatLngBounds(result['southwest'], result['northeast'])
    elif isinstance(result, (list, tuple)):
        for index in xrange(len(result)):
            result[index] = _parseGeocoderResult(result[index])
    return result


class MapsEventListener(list):
    pass


class _event(object):
    def addListener(self, instance, eventName, handlerName):
        listener = MapsEventListener([eventName, handlerName])
        instance.setdefault('evt', []).append(listener)
        listener.instance = instance
        return listener

    def addListenerOnce(self, instance, eventName, handlerName):
        listener = MapsEventListener([eventName, handlerName, True])
        instance.setdefault('evt', []).append(listener)
        listener.instance = instance
        return listener

    def clearInstanceListeners(self, instance):
        if 'evt' in instance:
            del instance['evt']

    def clearListeners(self, instance, eventName):
        if 'evt' in instance:
            for listener in instance['evt']:
                if listener[0] == eventName:
                    instance['evt'].remove(listener)
            if not instance['evt']:
                del instance['evt']

    def removeListener(self, listener):
        instance = listener.instance
        if 'evt' in instance:
            if listener in instance['evt']:
                instance['evt'].remove(listener)
            if not instance['evt']:
                del instance['evt']


event = _event()


class LatLng(MapClass):
    """A point in geographical coordinates, latitude and longitude.

    Equivalent to google.maps.LatLng. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.LatLng instance.

    """

    def __init__(self, lat, lng, noWrap=None):
        super(LatLng, self).__init__(cls='LatLng')
        self['arg'] = Args(['lat', 'lng', 'noWrap'], [Degree(lat), Degree(lng)])
        if noWrap is not None:
            self['arg'].setdefault('noWrap', noWrap)

    def __unicode__(self):
        return self.toUrlValue()

    def equals(self, other):
        return (self.lat() == other.lat() and self.lng() == other.lng())

    def lat(self):
        return self['arg'].get('lat')

    def lng(self):
        return self['arg'].get('lng')

    def toString(self):
        return '(%s, %s)' % (self.lat(), self.lng())

    def toUrlValue(self, precision=6):
        return '%s,%s' % (Degree(self.lat(), precision),
                          Degree(self.lng(), precision))


class LatLngBounds(MapClass):
    """A rectangle in geographical coordinates.

    Equivalent to google.maps.LatLngBounds. When parsed by
    JSONEncoder and subsequently by our custom jQuery plugin,
    it will be converted to an actual google.maps.LatLngBounds
    instance.

    """

    def __init__(self, sw=None, ne=None):
        super(LatLngBounds, self).__init__(cls='LatLngBounds')
        self['arg'] = Args(['sw', 'ne'])
        if sw:
            self['arg'].setdefault('sw', sw)
        if ne:
            self['arg'].setdefault('ne', ne)

    def __unicode__(self):
        return self.toUrlValue()

    def equals(self, other):
        # Check if our corners are equal.
        return (self.getSouthWest().equals(other.getSouthWest()) and
                self.getNorthEast().equals(other.getNorthEast()))

    def getNorthEast(self):
        return self['arg'].get('ne')

    def getSouthWest(self):
        return self['arg'].get('sw')

    def isEmpty(self):
        return ((not self.getSouthWest()) or
                (self.getNorthEast() and
                 self.getSouthWest().lat() >
                 self.getNorthEast().lat()))

    def toString(self):
        return '(%s, %s)' % (self.getSouthWest().toString(),
                             self.getNorthEast().toString())

    def toUrlValue(self, precision=6):
        return '%s,%s' % (self.getSouthWest().toUrlValue(precision),
                          self.getNorthEast().toUrlValue(precision))


class Point(MapClass):
    """A point on a two-dimensional plane.

    Equivalent to google.maps.Point. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Point instance.

    """

    def __init__(self, x, y):
        super(Point, self).__init__(cls='Point')
        self['arg'] = Args(['x', 'y'], [x, y])

    def __unicode__(self):
        return '%s,%s' % (self['arg'].get('x', 0),
                          self['arg'].get('y', 0))

    def _getX(self):
        return self['arg'][0]

    def _getY(self):
        return self['arg'][1]

    def _setX(self, x):
        self['arg'][0] = x

    def _setY(self, y):
        self['arg'][1] = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def toString(self):
        return '(%s, %s)' % (self.x, self.y)

    x = property(_getX, _setX)

    y = property(_getY, _setY)


class Size(MapClass):
    """A two-dimensonal size.

    Equivalent to google.maps.Size. When parsed by JSONEncoder
    and subsequently by our custom jQuery plugin, it will be
    converted to an actual google.maps.Size instance.

    """

    def __init__(self, width, height, widthUnit=None, heightUnit=None):
        super(Size, self).__init__(cls='Size')
        self['arg'] = Args(['width', 'height', 'widthUnit', 'heightUnit'],
                           [int(width), int(height)])
        if widthUnit:
            self['arg'].setdefault('widthUnit', widthUnit)
        if heightUnit:
            self['arg'].setdefault('heightUnit', heightUnit)

    def __unicode__(self):
        return '%sx%s' % (self['arg'].get('width', 0),
                          self['arg'].get('height', 0))

    def _getHeight(self):
        return self['arg'][1]

    def _getWidth(self):
        return self['arg'][0]

    def _setHeight(self, height):
        self['arg'][1] = height

    def _setWidth(self, width):
        self['arg'][0] = width

    def equals(self, other):
        return self.width == other.width and self.height == other.height

    def toString(self):
        return '(%s, %s)' % (self.width, self.height)

    height = property(_getHeight, _setHeight)

    width = property(_getWidth, _setWidth)


class Degree(float):
    """A custom float class for degrees.

    For holding degrees of a circle (latitude and longitude).
    When converted to a string or parsed by JSONEncoder, it
    will output with, at most, the specified precision.

    """

    def __new__(cls, value, precision=6):
        return float.__new__(cls, value)

    def __init__(self, value, precision=6):
        self.precision = precision

    def __repr__(self):
        return (('%%0.%df' % self.precision) % self).rstrip('0').rstrip('.')

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Args(list):
    """A custom list that implements setdefault and get by name."""

    def __init__(self, names, values=None):
        super(Args, self).__init__(values or [])
        self.names = names

    def get(self, name, default=None):
        i = self.names.index(name)
        return self[i] if len(self) > i else default

    def setdefault(self, name, default=None):
        i = self.names.index(name)
        if len(self) <= i or self[i] is None:
            # Fill gaps with None.
            self.extend(None for _ in xrange(len(self), i))
            self.append(default)
        return self[i]
