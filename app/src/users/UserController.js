(function () {

    angular
        .module('users')
        .controller('UserController', [
            'userService', '$mdSidenav', '$mdBottomSheet', '$log', '$q', '$http',
            UserController
        ]);

    /**
     * Main Controller for the Angular Material Starter App
     * @param $scope
     * @param $mdSidenav
     * @param avatarsService
     * @constructor
     */
    function UserController(userService, $mdSidenav, $mdBottomSheet, $log, $q, $http) {
        var self = this;

        self.selected = null;
        self.users = [];
        self.selectUser = selectUser;
        self.toggleList = toggleUsersList;
        self.share = share;
        $http.post('/accounts_api/register/', {
            last_name: 'my_ce',
            first_name: 'my_face',
            email: 'my_face@asd.de',
            password: 'm',
            gender: 'm'
        }).
            success(function (data, status, headers, config) {
                // this callback will be called asynchronously
                // when the response is available
            }).
            error(function (data, status, headers, config) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        // Load all registered users

        userService
            .loadAllUsers()
            .then(function (users) {
                self.users = [].concat(users);
                self.selected = users[0];
            });

        // *********************************
        // Internal methods
        // *********************************

        /**
         * First hide the bottomsheet IF visible, then
         * hide or Show the 'left' sideNav area
         */
        function toggleUsersList() {
            var pending = $mdBottomSheet.hide() || $q.when(true);

            pending.then(function () {
                $mdSidenav('left').toggle();
            });
        }

        /**
         * Select the current avatars
         * @param menuId
         */
        function selectUser(user) {
            self.selected = angular.isNumber(user) ? $scope.users[user] : user;
            self.toggleList();
        }

        /**
         * Show the bottom sheet
         */
        function share($event) {
            var user = self.selected;

            $mdBottomSheet.show({
                parent: angular.element(document.getElementById('content')),
                templateUrl: '/static/src/users/view/contactSheet.html',
                controller: ['$mdBottomSheet', UserSheetController],
                controllerAs: "vm",
                bindToController: true,
                targetEvent: $event
            }).then(function (clickedItem) {
                clickedItem && $log.debug(clickedItem.name + ' clicked!');
            });

            /**
             * Bottom Sheet controller for the Avatar Actions
             */
            function UserSheetController($mdBottomSheet) {
                this.user = user;
                this.items = [
                    {
                        name: 'Phone',
                        icon: 'phone',
                        icon_url: '/static/assets/svg/phone.svg'
                    },
                    {
                        name: 'Twitter',
                        icon: 'twitter',
                        icon_url: '/static/assets/svg/twitter.svg'
                    },
                    {
                        name: 'Google+',
                        icon: 'google_plus',
                        icon_url: '/static/assets/svg/google_plus.svg'
                    },
                    {
                        name: 'Hangout',
                        icon: 'hangouts',
                        icon_url: '/static/assets/svg/hangouts.svg'
                    }
                ];
                this.performAction = function (action) {
                    $mdBottomSheet.hide(action);
                };
            }
        }

    }

})();
