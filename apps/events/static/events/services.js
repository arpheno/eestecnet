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
        }]);

