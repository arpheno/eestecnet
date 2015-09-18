/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.commitments.create', ['ngRoute', "eestec.commitments.services"])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities/new/', {
            templateUrl: '/static/commitments/views/create.html',
            controller: 'CommitmentCreate'
        });
    }])
    .controller('CommitmentCreate', ["$scope","Commitment", function ($scope, Commitment) {
        $scope.Commitment = Commitment;
    }]);
