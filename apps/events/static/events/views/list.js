/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.list', ['ngRoute',
    'eestec.events.services'
])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/events/', {
            templateUrl: 'static/events/views/list.html',
            controller: 'EventListCtrl'
        });
    }])

    .controller('EventListCtrl', ['$scope', 'Event', function ($scope, Event) {
        $scope.events = Event.query();
        console.log($scope.events);
    }]);
