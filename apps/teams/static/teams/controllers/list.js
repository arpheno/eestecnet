/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.teams.list', ['ngRoute',
    'eestec.teams.services'
])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/', {
            templateUrl: '/static/teams/views/list.html',
            controller: 'CommitmentListController'
        });
    }])
    .controller('CommitmentListController', ["$scope", "Commitment",
        function ($scope, Commitment) {
            $scope.object_list = Commitment.query();
        }])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/teams/', {
            templateUrl: '/static/teams/views/list.html',
            controller: 'TeamListController'
        });
    }])
    .controller('TeamListController', ["$scope", "Team",
        function ($scope, Team) {
            $scope.object_list = Team.query();
        }]);
