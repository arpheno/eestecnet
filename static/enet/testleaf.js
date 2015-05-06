var map;
var ajaxRequest;
var plotlist;
var plotlayers = [];

$(function () {
    // set up the map
    L.Icon.Default.imagePath = '/static/leaflet/images/'
    map = new L.Map('map');
    // create the tile layer with correct attribution
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var mapBox = 'http://{s}.tiles.mapbox.com/v3/Sebastian Wozny.iojo68jj/{z}/{x}/{y}.png';
    var osmAttrib = 'Map data © <a href="http://mapbox.com">Mapbox</a> contributors';
    var osm = new L.TileLayer(mapBox, {minZoom: 2, maxZoom: 12, attribution: osmAttrib});

    // start the map in South-East England
    map.setView(new L.LatLng(49.7, 9.14), 4);
    map.addLayer(osm);
});
