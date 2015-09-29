/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.detail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/events/:pk/', {
            templateUrl: '/static/events/views/detail.html',
            controller: 'EventDetailController'
        });
    }])

    .controller('EventDetailController', [
        "$scope", "Event", "$routeParams",
        function ($scope, Event, $routeParams) {
            $scope.object = Event.get({pk: $routeParams.pk});
        }]);

