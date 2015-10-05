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
                    console.log($scope.fields);
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
        var imagecropcontroller = ["$scope", "$mdDialog",
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
        ];
        var control_initialization = ["$scope", function ($scope) {
            $scope.$watch($scope.res, function () {
                var timeout = 1000;
                var contentfetching = setInterval(function () {
                        if ($scope.res.images[$scope.req]) {
                        $scope.attrs.$set('ngSrc', $scope.res.images[$scope.req].full_size);
                        clearInterval(contentfetching);
                    }
                }, timeout);
            }, true);
            $scope.update = function () {
                $scope.res[$scope.req] = $scope.element.text();
                $scope.res.$update();
            };
        }];
        return {
            restrict: 'A', // only activate on element attribute
            scope: {res: '=', req: '='},
            controller: control_initialization,
            link: function ($scope, element, attrs) {
                $scope.attrs = attrs;
                $scope.update = function (image) {
                    $scope.source = image;
                    attrs.$set('ngSrc', image);
                    $scope.res.images[$scope.req] = {full_size: image};
                    $scope.res.$update();
                };
                element.on('click', function (ev) {
                    $mdDialog.show({
                        templateUrl: '/static/common/imgcrop.html',
                        controller: imagecropcontroller,
                        targetEvent: ev,
                        clickOutsideToClose: true,
                        escapeToClose: true
                    }).then($scope.update);
                });
            }
        };
    }])
    .directive('contenteditable', ["$q", function ($q) {
        return {
            restrict: 'A', // only activate on element attribute
            scope: {
                res: '=',
                req: '='
            },
            controller: ["$scope", function ($scope) {
                $scope.$watch($scope.res, function () {
                        var timeout = 1000;
                    var contentfetching = setInterval(function () {
                        if($scope.res[$scope.req]){
                            $scope.element.html($scope.res[$scope.req]);
                            clearInterval(contentfetching);
                        }
                    }, timeout);
                }, true);
                $scope.update = function () {
                    $scope.res[$scope.req] = $scope.element.text();
                    $scope.res.$update();
                };
            }],
            link: function (scope, element, attrs) {
                scope.element = element;
                element.on('focus', function () {
                    element.text(element.html());
                    scope.update();
                });
                element.on('blur', function () {
                    element.html(element.text());
                    scope.update();
                });
            }
        }
    }]);

