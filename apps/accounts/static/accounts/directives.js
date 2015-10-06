angular.module('eestec.accounts.directives', ['angular-jwt'])
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
                $scope.signup = function () {
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
                        $mdDialog.hide({token: response.data.token, permanent: $scope.login.permanent});
                    }, function (response) {
                        console.log("FAIL");
                    });
                }
            }];
        var controller = ["$scope", "$mdDialog", "$http", "$localStorage", "$location", "$route", "$sessionStorage","jwtHelper",
                function ($scope, $mdDialog, $http, $localStorage, $location, $route, $sessionStorage,jwtHelper) {
                    $scope.$on('$routeChangeSuccess', function () {
                        //If this doesn't work, console.log $route.current to see how it's formatted
                        if ($location.path().indexOf("signin") > -1)
                            $scope.showLogin();
                    });
                    $scope.update = function (ev) {
                        $location.path("/people/"+$scope.user.id+"/").replace();
                    };
                    $scope.logout = function (ev) {
                        $localStorage.token = "";
                    };
                    $scope.login = function (result) {
                        if (result.permanent) {
                            $localStorage.token = result.token;
                            $sessionStorage.token = "";
                        } else {
                            $sessionStorage.token = result.token;
                            $sessionStorage.token = "";
                        }
                        $scope.set_user();
                        if ($location.path().indexOf("signin") > -1) {
                            $location.path("/").replace();
                        }
                    };
                    $scope.refresh_token = function () {
                        if ($localStorage.token &&!jwtHelper.isTokenExpired($localStorage.token)) {
                            console.log( jwtHelper.decodeToken($localStorage.token));
                            $http({
                                url: "/api-token-refresh/",
                                method: "POST",
                                data: {token:$localStorage.token}
                            }).then($scope.login);
                        }else{
                            $localStorage.token="";
                        }
                    };
                    $scope.refresh_token();
                    $scope.set_user = function () {
                        if ($localStorage.token) {
                            $http.get("/api/accounts/me/").then(function (result) {
                                $scope.user = result.data;
                            });
                        }
                    };
                    $scope.showLogin = function (ev) {
                        $mdDialog.show({
                            controller: dialogController,
                            templateUrl: '/static/accounts/login.html',
                            clickOutsideToClose: true,
                            escapeToClose: true
                        }).then($scope.login);
                    };
                }

            ]
            ;
        return {
            restrict: 'E',
            scope: {user: '='},
            templateUrl: "/static/accounts/area.html",
            controller: controller
        };
    }]
)
;


