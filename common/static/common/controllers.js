/**
 * Created by swozn on 9/19/2015.
 */
angular.module('eestec.common.controllers', [
    'ngMaterial',
    'uiGmapgoogle-maps'
])
    .controller('networkController', ["$scope", "uiGmapGoogleMapApi", "Commitment",
        function ($scope, uiGmapGoogleMapApi,Commitment) {
        $scope.map = "";
        $scope.events = {
            "scroll": function () {
                // Override the scroll event so it doesnt zoom the map.
                // This is important for mobile devices.
                return;
            }
        };
        uiGmapGoogleMapApi.then(function (maps) {
            $scope.map = {
                center: {
                    latitude: 48.1333,
                    longitude: 11.56
                },
                zoom: 5
            };
        });
        $scope.commitments = Commitment.query(function (result) {
            $scope.markers = result.filter(function (x) {
                return x.locations.length;
            }).map(function (x) {
                return JSON.parse(JSON.stringify(x.locations[0]));
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
