/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.services', ['ngResource'])
    .factory('Event', ['$resource',
        function ($resource) {
            return $resource('/api/events/:pk/', {pk: "@pk"},
                {});
        }])
    .factory('Workshop', ['$resource',
        function ($resource) {
            return $resource('/api/workshops/:pk/', {pk: "@pk"},
                {});
        }])
    .factory('Exchange', ['$resource',
        function ($resource) {
            return $resource('/api/exchanges/:pk/', {pk: "@pk"},
                {});
        }])
    .factory('IMW', ['$resource',
        function ($resource) {
            return $resource('/api/imws/:pk/', {pk: "@pk"},
                {});
        }]);

