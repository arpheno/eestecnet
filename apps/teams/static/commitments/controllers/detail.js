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

    .controller('CommitmentDetailController', ["$scope",function ($scope) {
        $scope.a = 0;
        console.log("a");

    }]);
