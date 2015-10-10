/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.accounts.detail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/people/:id/', {
            templateUrl: '/static/accounts/views/detail.html',
            controller: 'AccountDetailController'
        });
    }])

    .controller('AccountDetailController', [
        "$scope","Account","$routeParams",
        function ($scope,Account,$routeParams) {
        $scope.object = Account.get({id:$routeParams.id});
    }]);
