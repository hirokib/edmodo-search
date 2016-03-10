angular.module('searchApp')
  .service('searchService', ['$http', function($http) {

    var _this = this;

    this.getAllProducts = function() {
      return $http.get('/api/v1/products');
    };

    this.getSearchResults = function(query) {
      return $http.get('/api/v1/products/'+query);
    }

    this.getFlaggedResults = function() {
      return $http.get('/api/v1/products/flagged');
    }

  }]);
