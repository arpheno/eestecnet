/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.commitments.list', ['ngRoute',
    'eestec.commitments.services'
])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/', {
            templateUrl: '/static/commitments/views/list.html',
            controller: 'CommitmentListController'
        });
        $routeProvider.when('/cities/:id', {
            templateUrl: '/static/commitments/views/detail.html',
            controller: 'CommitmentController'
        });
    }])

    .controller('CommitmentListController',[ "$scope","Commitment",function ($scope, Commitment) {
        $scope.commitments = Commitment.query();
        console.log($scope.commitments);
    }])

    .controller('CommitmentController',[ "$scope","Commitment", "$routeParams", "$log", function ($scope, Commitment, $routeParams, $log) {
        $scope.test = $routeParams.id;
        $scope.commitments = Commitment.query(5);
        console.log($scope.commitments);
        // console.log($scope.test);
        // $log.debug($scope.test);
    }]);
