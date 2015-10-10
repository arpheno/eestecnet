/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.commitments.detail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/:pk', {
            templateUrl: '/static/commitments/views/detail.html',
            controller: 'CommitmentDetailController'
        });
    }])

    .controller('CommitmentDetailController',[ "$scope","Commitment", "$routeParams", "$log", function ($scope, Commitment, $routeParams, $log) {
        var pk = $routeParams.pk;
        Commitment.get({pk:pk},
            function(commitment) {
                $scope.commitment = commitment;
            });
    }]);
