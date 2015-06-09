/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.events.services', ['ngResource'])
    .factory('Event', ['$resource',
        function ($resource) {
            return $resource('http://localhost:8000/api/events/:pk', {pk: "@pk"}, {});
        }]);
