/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.create', ['ngRoute', "eestec.events.services"])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/new/', {
            templateUrl: '/static/events/views/create.html',
            controller: 'EventCreate'
        });
    }])
    .controller('EventCreate', ["$scope","Event", function ($scope, Event) {
        $scope.Event = Event;
    }]);
