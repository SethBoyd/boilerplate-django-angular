'use strict';

/**
 * @ngdoc function
 * @name myprojectApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the myprojectApp
 */
angular.module('myprojectApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

  $scope.demo = "API call did not work, did you start the server?"

  $http.get('/api/demo/').success(function(data){
    $scope.demo = data.message;
  });


  });
