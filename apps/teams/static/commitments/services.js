/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.commitments.services', ['ngResource'])
    .factory('Commitment', ['$resource',
        function ($resource) {
            return $resource('/api/commitments/:pk/', {pk: "@pk"}, {});
        }]);

