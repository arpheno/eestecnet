/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.common.services', ['ngResource'])
    .factory('Content', ['$resource',
        function ($resource) {
            return $resource('/api/content/:id/', {id: "@id"}, {
                'update': {method: 'PUT'}
            });
        }]);
