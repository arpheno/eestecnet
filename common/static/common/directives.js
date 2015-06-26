angular.module('customControl', []).
    directive('contenteditable', [function () {
        return {
            restrict: 'A', // only activate on element attribute
            scope: {
                res: '=',
                req: '='

            },
            link: function (scope, element, attrs) {
                console.log(attrs);
                element.html(scope.res[scope.req]);
                // Listen for change events to enable binding
                element.on('focus', function () {
                    element.text(element.html());
                    scope.res.$update();
                });
                element.on('blur', function () {
                    scope.res[scope.req] = element.text();
                    element.html(element.text());
                    scope.res.$update();
                });
            }
        };
    }]);
