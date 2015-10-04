/**
 * Created by swozn on 9/19/2015.
 */
angular.module('eestec.common.controllers', [
    'ngMaterial',
    'ngMap'
])
    .controller('networkController', ["$scope","Commitment",
        function ($scope, Commitment) {
            Commitment.query(function (result) {
                $scope.markers = result.filter(function (x) {
                    return x.locations.length;
                }).map(function (x) {
                    console.log(x);
                    return {pos: x.locations[0].latitude+","+ x.locations[0].longitude}
                });
            });
        }])
    .controller('toolbarController', [
        "$scope", "$location", "$mdDialog", "$mdSidenav", "$http",
        function ($scope, $location, $mdDialog, $mdSidenav, $http) {
            $scope.navigation = function (name) {
                $location.path(name).replace();
                console.log($location);
            };
            $scope.toggleSidenav = function (name) {
                $mdSidenav(name).toggle();
            };
        }])
    .controller('appCtrl', [
        '$scope',
        function ($scope) {
            $scope.user = "";
        }])
    .controller('contentController', [
        '$scope', 'Content', "$q",
        function ($scope, Content, $q) {
            CONTENTLOADED = $q.defer();
            $scope.contents = Content.query(function () {
                $scope.content = function (name) {
                    var result = $scope.contents.filter(function (x) {
                        return x.name === name;
                    })[0];
                    if (!result) {
                        result = new Content();
                        result.name = name;
                        result.content = "Placeholder for " + name;
                        result.images = [];
                        result.$save();
                        $scope.contents.push(result);
                    }
                    return result;
                };
                CONTENTLOADED.resolve();
            });
            $scope.edit = false;
        }]);
