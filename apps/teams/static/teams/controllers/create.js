/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.teams.create', ['ngRoute', "eestec.teams.services"])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/new/', {
            templateUrl: '/static/teams/views/create.html',
            controller: 'CommitmentCreate'
        });
    }])
    .controller('CommitmentCreate', ["$scope","Commitment", function ($scope, Commitment) {
        $scope.endpoint = Commitment;
    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/teams/new/', {
            templateUrl: '/static/teams/views/create.html',
            controller: 'TeamCreate'
        });
    }])
    .controller('TeamCreate', ["$scope","Team", function ($scope, Team) {
        $scope.endpoint = Team;
    }]);
