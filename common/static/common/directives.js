angular.module('eestec.common.directives', [
    'ngImgCrop'
])
    .directive('resourceform', [function () {
        return {
            restrict: 'E',
            scope: {
                resource: "="
            },
            link: function ($scope, element, attrs) {
                console.log($scope.resource);
                var resource = new $scope.resource;
                $scope.fields = resource.$options(function (value) {
                    $scope.fields = value.actions.POST;
                    $scope.headline = value.name.split(" ");
                    $scope.headline.pop();
                    $scope.headline = $scope.headline.join(" ");
                });
                $scope.obj = new $scope.resource;
            },
            templateUrl: "/static/common/resourceform.html",
            controller: function ($scope) {
                console.log($scope.resource);
            }
        };
    }])
    .directive('editable', ['$mdDialog', '$q', function ($mdDialog, $q) {
        return {
            restrict: 'A', // only activate on element attribute
            scope: {
                res: '=',
                req: '='

            },
            link: function ($scope, element, attrs) {
                if (!CONTENTLOADED) {
                    CONTENTLOADED = $q.defer();
                }
                CONTENTLOADED.promise.then(function () {
                    console.log(JSON.stringify(CONTENTLOADED));
                    if ($scope.res.images[$scope.req]) {
                        attrs.$set('ngSrc', $scope.res.images[$scope.req].full_size);
                    }
                    element.on('click', function (ev) {
                        console.log(ev);
                        $mdDialog.show({
                            controller: ["$scope", "$mdDialog",
                                function ($scope, $mdDialog) {
                                    $scope.hide = $mdDialog.hide;
                                    $scope.cancel = $mdDialog.cancel;
                                    $scope.confirm = function () {
                                        $mdDialog.hide($scope.myCroppedImage);
                                    };
                                    $scope.myImage = '';
                                    $scope.myCroppedImage = '';
                                    console.log("trying to show log");

                                    var handleFileSelect = function (evt) {
                                        var file = evt.currentTarget.files[0];
                                        var reader = new FileReader();
                                        reader.onload = function (evt) {
                                            $scope.$apply(function ($scope) {
                                                $scope.myImage = evt.target.result;
                                            });
                                        };
                                        reader.readAsDataURL(file);
                                    };
                                    angular.element(document).ready(function () {
                                            var temp = document.getElementById('fileInput');
                                            angular.element(temp).on('change', handleFileSelect);
                                        }
                                    );
                                }
                            ],
                            templateUrl: '/static/common/imgcrop.html',
                            targetEvent: ev,
                            clickOutsideToClose: true,
                            escapeToClose: true
                        })
                            .then(function (image) {
                                $scope.source = image;
                                attrs.$set('ngSrc', image);
                                $scope.res.images[$scope.req] = {
                                    full_size: image
                                };
                                $scope.res.$update();
                            }, function () {
                                $scope.alert = 'You cancelled the dialog.';
                            });
                    });
                });
            }
        };
    }]).
    directive('contenteditable', ["$q", function ($q) {
        return {
            restrict: 'A', // only activate on element attribute
            scope: {
                res: '=',
                req: '='
            },
            link: function (scope, element, attrs) {
                if (!CONTENTLOADED) {
                    CONTENTLOADED = $q.defer();
                }
                CONTENTLOADED.promise.then(function () {
                    result = scope.res;
                    element.html(result[scope.req]);
                    // Listen for change events to enable binding
                    element.on('focus', function () {
                        element.text(element.html());
                        result.$update();
                    });
                    element.on('blur', function () {
                        result[scope.req] = element.text();
                        element.html(element.text());
                        result.$update();
                    });
                })
            }
        };
    }]).
    directive('account', [function () {
        var dialogController = ["$scope", "$mdDialog", "$http",
            function ($scope, $mdDialog, $http) {
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
                        templateUrl: '/static/common/login.html',
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


