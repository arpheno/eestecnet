/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.detail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/events/:pk', {
            templateUrl: 'static/events/detail.html',
            controller: 'EventDetailCtrl'
        });
    }])

    .controller('EventDetailCtrl', ["$scope",function ($scope) {
        $scope.a = 0;
        console.log("a");

    }]);
