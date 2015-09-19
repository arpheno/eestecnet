/**
 * Created by swozn on 9/19/2015.
 */
angular.module('eestec.common.controllers', [
    'ngMaterial',
    'uiGmapgoogle-maps'
])
    .controller('networkController', ["$scope", "uiGmapGoogleMapApi", function ($scope, uiGmapGoogleMapApi) {
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
    }])
    .controller('appCtrl', [
        '$scope', '$http', '$location', '$mdDialog', '$mdSidenav', 'Content',
        function ($scope, $http, $location, $mdDialog, $mdSidenav, Content) {
            $scope.contents = Content.query(function () {
                var dict = {};
                for (var i = 0; i < $scope.contents.length; i++) {
                    dict[$scope.contents[i].name] = $scope.contents[i];
                }
                $scope.contents = dict;
                console.log($scope.contents);
            });
            //$scope.content = function (name) {
            //    var deferred = $q.defer();
            //    console.log("my ass");
            //
            //    $scope.contents.$promise.then(function (r) {
            //        var result = $scope.contents.filter(function (x) {
            //            return x.name === name;
            //        })[0];
            //        if (!result) {
            //            result = new Content();
            //            result.name = name;
            //            result.content = "Placeholder for " + name;
            //            result.images = [];
            //            result.$save();
            //            $scope.contents.push(result);
            //        }
            //        deferred.resolve(result);
            //    });
            //    return deferred.promise;
            //};
            $scope.edit = false;
            $scope.toggleSidenav = function (name) {
                $mdSidenav(name).toggle();
            };
            $scope.navigation = function (name) {
                $location.path(name).replace();
                console.log($location);

            };
            $scope.showLogin = function (ev) {
                $mdDialog.show({
                    controller: ["$scope", "$mdDialog", function ($scope, $mdDialog) {
                        $scope.hide = $mdDialog.hide;
                        $scope.cancel = $mdDialog.cancel;
                        $scope.answer = function (answer) {
                            $mdDialog.hide(answer);
                        };
                    }],
                    templateUrl: '/static/common/login.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    escapeToClose: true
                })
            };
        }]);
