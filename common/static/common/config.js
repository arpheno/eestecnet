/**
 * Created by swozn on 9/19/2015.
 */
angular.module('eestec.common.config', [
    'ngRoute',
    'ngMaterial'
])
    .config(["$resourceProvider", function ($resourceProvider) {
        $resourceProvider.defaults.actions = {
            'get': {method: 'GET'},
            'save': {method: 'POST'},
            'query': {method: 'GET', isArray: true},
            'remove': {method: 'DELETE'},
            'delete': {method: 'DELETE'},
            'update': {method: 'PUT'},
            'options': {method: 'OPTIONS'}
        };
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'static/common/identity.html'
        });
        $routeProvider.when('/identity/', {
            templateUrl: 'static/common/identity.html'
        });
    }])
    .config(['$locationProvider', function ($locationProvider) {
        $locationProvider.html5Mode(true);
    }])
    .config(["uiGmapGoogleMapApiProvider", function (uiGmapGoogleMapApiProvider) {
        uiGmapGoogleMapApiProvider.configure({
            //    key: 'your api key',
            v: '3.17',
            libraries: 'weather,geometry,visualization'
        });
    }])
    .config(["$httpProvider", function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])
    .config(["$mdThemingProvider", function ($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('red')
            .accentPalette('light-blue');
    }]);
