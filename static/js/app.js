(function() {

  'use strict';

  var searchApp = angular.module('searchApp', ['ngRoute']);

  searchApp.config(['$routeProvider',
    function($routeProvider) {
      $routeProvider
        .when('/', {
          templateUrl: 'partial/results.html',
          controller: 'searchResultsCtrl',
          controllerAs: 'results'
        })

      .when('/flagged', {
        templateUrl: 'partial/flagged-results.html',
        controller: 'searchRatingsCtrl',
        controllerAs: 'ratings'
      })

      .otherwise({
        redirectTo: '/'
      });

    }
  ])

}());
