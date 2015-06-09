'use strict';

// Declare app level module which depends on views, and components
angular.module('eestec', [
    'ngRoute',
    'ngMaterial',
    'ngMdIcons',
    'eestec.events'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/'});
    }]).
    config(function ($resourceProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }).
    config(['$locationProvider', function ($locationProvider) {
        $locationProvider.html5Mode(true);
    }]).
    controller('appCtrl', [
        '$scope', '$mdSidenav', '$location', function ($scope, $mdSidenav, $location) {
            $scope.toggleSidenav = function (name) {
                $mdSidenav(name).toggle();
            };
            $scope.navigation = function (name) {
                $location.path(name).replace();
                console.log($location);
                ;
            }
        }]);