(function() {

  'use strict';

  angular.module('searchApp')
    .controller('searchResultsCtrl1', ['$scope', '$http', 'searchService', function($scope, $http, searchService) {
      this.searchResults = $scope.searchResults;
      this.test1 = $scope.test;


    }]);

    angular.module('searchApp')
      .controller('searchRatingsCtrl', ['$scope', '$http', 'searchService', function($scope, $http, searchService) {

        var _this = this;
        this.ratingList = [];
        searchService.getFlaggedResults().then(function(response){
          console.log(response.data);
          _this.ratingList = response.data;
        });


      }]);

  angular.module('searchApp')
    .controller('searchResultsCtrl', ['$scope', '$http', 'searchService', function($scope, $http, searchService) {
      $scope.data = searchService;
      $scope.query = '';
      $scope.lastQuery = '';
      $scope.searchResults = [{
        "_id": 304599,
        "_score": 0.47027928,
        "img_path": "https://media-market.edmodo.com/media/public/194cd8be95ef13a2e469367ef69c233bb3f78ec6.png",
        "long_desc": "",
        "title": "Literature Test 3"
      }];
      $scope.test = 'hello babe';

      // console.log(searchService.getAllProducts().then(function(results) {
      //   $scope.searchResults = results;
      // }));
      // $scope.$watch('searchResults', function(newValue, oldValue) {
      //   $scope.searchResults = newValue;
      // });
      $scope.$watch('$scope.searchResults', function() {
        $scope.searchResults = $scope.searchResults;
      });


      $scope.search = function() {
        console.log('hit search');
        if ($scope.query != '') {
          console.log($scope.query);
          // $scope.searchResults = searchService.getAllProducts();
          searchService.getSearchResults($scope.query).then(function(response) {
            //Dig into the responde to get the relevant data
            console.log(response.data);
            // $scope.searchResults = response.data;
            angular.copy(response.data, $scope.searchResults);
            console.log($scope.searchResults);
          });

          // console.log($scope.searchResults);

          // $scope.lastQuery = $scope.query;
          // $http({
          //   method: "GET",
          //   url: "api/v1/products/" + $scope.query
          // }).then(function mySucces(response) {
          //   $scope.$apply(function(){
          //     $scope.searchResults = response.data;
          //   });
          //   console.log($scope.searchResults);
          // }, function myError(response) {
          //   $scope.searchResults = response.statusText;
          // });
          $scope.query = '';
        }
      };

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

      $scope.addResultFlags = function(query, product_id, resultFlags) {
        console.log(query);
        console.log(product_id);
        console.log(resultFlags);
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
  // end controller



}());
