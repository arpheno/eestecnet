/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.accounts.list', ['ngRoute',
    'eestec.accounts.services'
])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/people/', {
            templateUrl: '/static/accounts/views/list.html',
            controller: 'AccountListController'
        });
        console.log("Meh")
        $routeProvider.when('/signin', {});
    }])


    .controller('AccountListController',[ "$scope","Account",function ($scope, Account) {
        $scope.object_list = Account.query();
    }]);
