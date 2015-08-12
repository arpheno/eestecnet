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
    }])

    .controller('CommitmentListController', function ($scope, Commitment) {
        $scope.commitments = Commitment.query();
        console.log($scope.commitments);
    });
