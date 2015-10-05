/**
 *
 * Created by Arphen on 06.06.2015.
 */
'use strict';

angular.module('eestec.commitments.services', ['ngResource'])
    .factory('BaseTeam', ['$resource',
        function ($resource) {
            return $resource('/api/baseteams/:pk/', {pk: "@pk"},
                {});
        }])
    .factory('Commitment', ['$resource',
        function ($resource) {
            return $resource('/api/commitments/:pk/', {pk: "@pk"},
                {});
        }])
    .factory('Team', ['$resource',
        function ($resource) {
            return $resource('/api/internationalteams/:pk/', {pk: "@pk"},
                {});
        }]);

