"""
>>> from apps.gmapi import maps

# Test Map creation.
>>> m = maps.Map()
>>> m
{'arg': ['div'], 'cls': 'Map'}

# Test setting and getting the map center.
>>> m.setCenter(maps.LatLng(38, -97))
>>> m.getCenter()
{'arg': [38, -97], 'cls': 'LatLng'}

# Test setting the map type.
>>> m.setMapTypeId(maps.MapTypeId.ROADMAP)
>>> m.getMapTypeId()
{'val': 'MapTypeId.ROADMAP'}

# Test setting and getting the zoom.
>>> m.setZoom(3)
>>> m.getZoom()
3

# Test LatLngBounds creation.
>>> b = maps.LatLngBounds(maps.LatLng(18, -119), maps.LatLng(53, -74))
>>> b
{'arg': [{'arg': [18, -119], 'cls': 'LatLng'}, {'arg': [53, -74], 'cls': 'LatLng'}],
'cls': 'LatLngBounds'}

# Test setting multiple options at once.
>>> m.setOptions({'center': maps.LatLng(0, 0), 'zoom': 4, 'mapTypeId':
maps.MapTypeId.SATELLITE})
>>> m
{'arg': ['div', {'mapTypeId': {'val': 'MapTypeId.SATELLITE'}, 'center': {'arg': [0,
0], 'cls': 'LatLng'}, 'zoom': 4}], 'cls': 'Map'}

# Test creating a marker.
>>> k = maps.Marker()
>>> k.setPosition(maps.LatLng(38, -97))
>>> k.setMap(m)
>>> k
{'arg': [{'position': {'arg': [38, -97], 'cls': 'LatLng'}}], 'cls': 'Marker'}

# Make sure the marker was added to the map.
>>> m
{'arg': ['div', {'mapTypeId': {'val': 'MapTypeId.SATELLITE'}, 'center': {'arg': [0,
0], 'cls': 'LatLng'}, 'zoom': 4}], 'mkr': [{'arg': [{'position': {'arg': [38, -97],
'cls': 'LatLng'}}], 'cls': 'Marker'}], 'cls': 'Map'}


"""
