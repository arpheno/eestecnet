/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.create', ['ngRoute', "eestec.events.services"])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/events/new/', {
                templateUrl: '/static/events/views/create.html',
                controller: 'EventCreate'
            });
        $routeProvider
            .when('/IMWs/new/', {
                templateUrl: '/static/events/views/create.html',
                controller: 'IMWCreate'
            });
        $routeProvider
            .when('/exchanges/new/', {
                templateUrl: '/static/events/views/create.html',
                controller: 'ExchangeCreate'
            });
        $routeProvider
            .when('/workshops/new/', {
                templateUrl: '/static/events/views/create.html',
                controller: 'WorkshopCreate'
            });
    }])
    .controller('EventCreate', ["$scope", "Event", function ($scope, Event) {
        $scope.endpoint = Event;
    }])
    .controller('IMWCreate', ["$scope", "IMW", function ($scope, IMW) {
        $scope.endpoint = IMW;
    }])
    .controller('WorkshopCreate', ["$scope", "Workshop", function ($scope, Workshop) {
        $scope.endpoint = Workshop;
    }])
    .controller('ExchangeCreate', ["$scope", "Exchange", function ($scope, Exchange) {
        $scope.endpoint = Exchange;
    }]);
