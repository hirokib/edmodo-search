angular.module('searchApp')
  .service('searchService', ['$http', function($http) {

    var _this = this;

    this.products = [];


    this.getAllProducts = function() {
      return $http.get('/api/v1/products');
    };

    this.getSearchResults = function(query) {
      return $http.get('/api/v1/products/'+query);
    }

    this.getSearchResults('test').then(function(response) {
      _this.products = response;
    });

    this.getFlaggedResults = function() {
      return $http.get('/api/v1/products/flagged');
    }

  }]);
