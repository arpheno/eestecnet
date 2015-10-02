///**
// *
// * Created by Arphen on 06.06.2015.
// */
//'use strict';
//
//angular.module('eestec.accounts.detail', ['ngRoute'])
//
//    .config(['$routeProvider', function ($routeProvider) {
//        $routeProvider.when('/people/:pk/', {
//            templateUrl: '/static/accounts/views/detail.html',
//            controller: 'AccountDetailController'
//        });
//    }])
//
//    .controller('AccountDetailController', [
//        "$scope","Account","$routeParams",
//        function ($scope,Account,$routeParams) {
//        $scope.object = Account.get({pk:$routeParams.pk});
//    }]);TODO