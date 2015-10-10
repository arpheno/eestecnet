/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.teams.detail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/:pk/', {
            templateUrl: '/static/teams/views/detail.html',
            controller: 'CommitmentDetailController'
        });
    }])
    .controller('CommitmentDetailController', ["$scope", function ($scope) {
        //TODO
    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/teams/:pk/', {
            templateUrl: '/static/teams/views/detail.html',
            controller: 'TeamDetailController'
        });
    }])
    .controller('TeamDetailController', ["$scope",
        function ($scope) {
            //TODO
        }]);
