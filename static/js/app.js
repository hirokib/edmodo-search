(function() {

  'use strict';

  var searchApp = angular.module('searchApp', ['ngRoute']);

  searchApp.config(['$routeProvider',
    function($routeProvider) {
      $routeProvider
        .when('/', {
          templateUrl: 'partial/results.html',
          controller: 'searchResultsCtrl1',
          controllerAs: 'results'
        })


      .otherwise({
        redirectTo: '/'
      });

    }
  ])

}());
