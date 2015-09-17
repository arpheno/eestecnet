'use strict';

// Declare app level module which depends on views, and components
angular.module('eestec', [
    'ngRoute',
    'ngMaterial',
    'ngMdIcons',
    'eestec.events',
    'eestec.commitments',
    'customControl',
    'content.services',
    'ngImgCrop',
    'uiGmapgoogle-maps'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'static/common/identity.html'
        });
        $routeProvider.when('/identity/', {
            templateUrl: 'static/common/identity.html'
        });
    }])
    .config(function ($resourceProvider) {
        $resourceProvider.defaults.actions = {
            'get': {method: 'GET'},
            'save': {method: 'POST'},
            'query': {method: 'GET', isArray: true},
            'remove': {method: 'DELETE'},
            'delete': {method: 'DELETE'},
            'update': {method: 'PUT'},
            'options': {method: 'OPTIONS'}
        };
        $resourceProvider.defaults.stripTrailingSlashes = false;

    })
    .config(['$locationProvider', function ($locationProvider) {
        $locationProvider.html5Mode(true);
    }])
    .config(function (uiGmapGoogleMapApiProvider) {
        uiGmapGoogleMapApiProvider.configure({
            //    key: 'your api key',
            v: '3.17',
            libraries: 'weather,geometry,visualization'
        });
    })
    .config(function ($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('red')
            .accentPalette('light-blue');
    })
    .controller('networkController', function ($scope, uiGmapGoogleMapApi) {
        $scope.map = "";
        $scope.events = {
            "scroll": function () {
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
    })
    .controller('appCtrl', [
        '$scope', '$http', '$mdSidenav', '$location', '$mdDialog', 'Content',"$q",
        function ($scope, $http, $mdSidenav, $location, $mdDialog, Content,$q) {
            $http.defaults.xsrfCookieName = "csrftoken";
            $http.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            $scope.contents = Content.query(function () {
                $scope.loaded = true;
            });
            console.log($scope);
            $scope.name = 'ello';
            $scope.content = function (name) {
              var deferred = $q.defer();
                console.log("my ass");
                $scope.contents.$promise.then(function (r) {
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
                    deferred.resolve(result);
                });
                return deferred.promise;
            };
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
                    controller: DialogController,
                    templateUrl: '/static/common/login.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    escapeToClose: true,

                })
                    .then(function (answer) {
                        $scope.alert = 'You said the information was "' + answer + '".';
                    }, function () {
                        $scope.alert = 'You cancelled the dialog.';
                    });
            };

        }]);
function DialogController($scope, $mdDialog) {
    $scope.hide = function () {
        $mdDialog.hide();
    };
    $scope.cancel = function () {
        $mdDialog.cancel();
    };
    $scope.answer = function (answer) {
        $mdDialog.hide(answer);
    };
}
