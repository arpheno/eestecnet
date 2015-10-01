angular.module('eestec.accounts.directives', [])
    .directive('account', [function () {
        var registerController = ["$scope", "$mdDialog", "$http",
            function ($scope, $mdDialog, $http) {
                $scope.submit = function () {
                    $http({
                        url: "/accounts_api/register/",
                        method: "POST",
                        data: $scope.account
                    }).then(function (response) {
                        console.log(response);
                        $mdDialog.hide();
                    }, function (response) {
                        console.log("FAIL");
                    });
                }
            }];
        var dialogController = ["$scope", "$mdDialog", "$http",
            function ($scope, $mdDialog, $http) {
                $scope.signup= function(){
                    $mdDialog.show({
                        controller: registerController,
                        templateUrl: '/static/accounts/register.html',
                        clickOutsideToClose: true,
                        escapeToClose: true
                    });
                };
                $scope.submit = function () {
                    $http({
                        url: "/api-token-auth/",
                        method: "POST",
                        data: $scope.login
                    }).then(function (response) {
                        $mdDialog.hide(response.data.token);
                    }, function (response) {
                        console.log("FAIL");
                    });
                }
            }];
        var controller = ["$scope", "$mdDialog", "$http", "$localStorage",
            function ($scope, $mdDialog, $http, $localStorage) {
                $scope.logout = function (ev) {
                    $localStorage.token = "";
                    $scope.user = "";
                };
                $scope.login = function (result) {
                    $localStorage.token = result;
                    $http.get("/api/accounts/me/").then(function (result) {
                        $scope.user = result.data;
                    });
                };
                $scope.showLogin = function (ev) {
                    $mdDialog.show({
                        controller: dialogController,
                        templateUrl: '/static/accounts/login.html',
                        clickOutsideToClose: true,
                        escapeToClose: true
                    }).then($scope.login);
                };
            }];
        return {
            restrict: 'E',
            scope: {user: '='},
            templateUrl: "/static/accounts/area.html",
            controller: controller
        };
    }]);


