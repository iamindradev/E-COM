var app = angular.module("app",['ngRoute']);
app.config([
    "$routeProvider",
    function ($routeProvider) {
      $routeProvider
        .when("/", {
          templateUrl: "defaulthm.html",
        })
        .when("/viewprofile", {
          templateUrl: "profile.html",
        })
        .when("/orders",{
            templateUrl:"orders.html"
        })
        .when("/wishlist",{
            templateUrl:"wishlist.html"
        })
    },
  ]);
app.controller("home" ,function($scope, $http){
  var items={
    name:
  }

})