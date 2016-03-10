(function() {

  'use strict';

  angular.module('searchApp')
    .controller('searchResultsCtrl', ['$scope', '$http', 'searchService', function($scope, $http, searchService) {
      var _this = this;
      this.searchResults = $scope.searchResults;

      this.hideModal = function(id) {
        var modal = "#flag-modal" + id;
        $(function() {
          $(modal).modal('hide');
        });

      };

      this.addResultFlags = function(query, product_id, resultFlags) {
        var config = {
          headers: {
            'Content-type': 'application/json'
          }
        }
        var data = {
          query: query,
          id: product_id,
          resultFlags: resultFlags
        }
        var data = JSON.stringify(data);
        $http.post('/api/v1/search-result-flags', data, config)
          .success(function(data, status, headers, config) {
            $scope.PostDataResponse = data;
          })
          .error(function(data, status, header, config) {
            $scope.ResponseDetails = "Data: " + data +
              "<hr />status: " + status +
              "<hr />headers: " + header +
              "<hr />config: " + config;
          });

        $scope.resetFlags();
      };

    }]);

  angular.module('searchApp')
    .controller('searchRatingsCtrl', ['$scope', '$http', 'searchService', function($scope, $http, searchService) {

      var _this = this;
      this.ratingList = [];
      searchService.getFlaggedResults().then(function(response) {
        _this.ratingList = response.data;
      });


    }]);

  angular.module('searchApp')
    .controller('searchCtrl', ['$scope', '$http', 'searchService', '$location', function($scope, $http, searchService, $location) {
      var _this = this;

      $scope.data = searchService;
      $scope.query = '';
      $scope.lastQuery = '';
      $scope.searchResults = [];
      $scope.modal = '';

      $scope.search = function() {
        if ($scope.query != '') {
          searchService.getSearchResults($scope.query).then(function(response) {
            //Dig into the response to get the relevant data
            angular.copy(response.data, $scope.searchResults);
          });


          $scope.lastQuery = $scope.query;
          $scope.query = '';
          changeLocation('/');
        }
      };

      function changeLocation(path) {
        $location.path(path);

      }

      $scope.lastProductId = ''

      $scope.lastProduct = function(id) {
        $scope.lastProductId = id;
      }

      $scope.resultFlags = {
        modalValue1: false,
        modalValue2: false,
        modalValue3: false,
        modalValue4: false
      };

      $scope.resetFlags = function() {
        $scope.resultFlags = {
          modalValue1: false,
          modalValue2: false,
          modalValue3: false,
          modalValue4: false
        };
      };

    }]);
  // end controller

}());
