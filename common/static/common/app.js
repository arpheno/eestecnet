'use strict';

// Declare app level module which depends on views, and components
angular.module('eestec', [
    'ngRoute',
    'ngMaterial',
    'ngMdIcons',
    'eestec.events',
    'customControl',
    'content.services'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'static/common/identity.html'
        });
        $routeProvider.when('/identity/', {
            templateUrl: 'static/common/identity.html'
        });
        $routeProvider.otherwise({redirectTo: '/'});
    }]).
    config(function ($resourceProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }).
    config(['$locationProvider', function ($locationProvider) {
        $locationProvider.html5Mode(true);
    }]).
    config(function ($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('red')
            .accentPalette('light-blue');
    }).
    controller('appCtrl', [
        '$scope', '$http', '$mdSidenav', '$location', '$mdDialog', 'Content',
        function ($scope, $http, $mdSidenav, $location, $mdDialog, Content) {
            $http.defaults.xsrfCookieName = "csrftoken";
            $http.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            $scope.contents = Content.query(function () {
                $scope.loaded = true;
            });
            $scope.content = function (name) {
                while (!$scope.loaded) {
                    var a = 0;
                }
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
                console.log(result);
                return result;
            };
            $scope.edit = false;
            $scope.x = "hello";
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
