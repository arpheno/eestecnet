/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.accounts.services', ['ngResource','ngMaterial'])
    .factory('Account', ['$resource',
        function ($resource) {
            return $resource('/api/accounts/:id/', {id: "@id"},
                {});
        }])
