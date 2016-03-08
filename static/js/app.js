(function() {

    'use strict';

    var searchApp = angular.module('searchApp', []);

    searchApp.controller('searchController', ['$scope', '$http', function($scope, $http) {

        $scope.query = '';
        $scope.lastQuery = '';
        $scope.searchResults = [];

        $scope.search = function() {
          if ($scope.query != '') {
            $scope.lastQuery = $scope.query;
            $http({
              method: "GET",
              url: "api/v1/products/" + $scope.query
            }).then(function mySucces(response) {
              $scope.searchResults = response.data;
            }, function myError(response) {
              $scope.searchResults = response.statusText;
            });
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
          // var data = $.param({
          //   query: query,
          //   id: product_id,
          //   resultFlags: resultFlags
          // });
          //
          var config = {
            headers: {
              'Content-type': 'application/json'
            }
          }

          var data = JSON.stringify('hi');
          $http.post('/api/v1/search-result-flags', data, {
              headers: {
                'Content-Type': 'application/json'
              })
            .success(function(data, status, headers, config) {
              $scope.PostDataResponse = data;
            })
            .error(function(data, status, header, config) {
              $scope.ResponseDetails = "Data: " + data +
                "<hr />status: " + status +
                "<hr />headers: " + header +
                "<hr />config: " + config;
            });

            // var data = {
            //   query: query,
            //   id: product_id,
            //   resultFlags: resultFlags
            // }
            //
            //
            // var req = {
            //   method: 'POST',
            //   url: '/api/v1/search-result-flags',
            //   headers: {
            //     'Content-Type': 'application/json'
            //   },
            //   data: {
            //     angular.toJson(data);
            //   }
            // }

            // $http(req).then(function successCallback(response) {
            //   console.log('success')
            // }, function errorCallback(response) {
            //   // called asynchronously if an error occurs
            //   // or server returns response with an error status.
            // });

          };


        }]);





    }());
