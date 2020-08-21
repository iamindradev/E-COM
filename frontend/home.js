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
  $http({
    method:"GET",
    url:"http://127.0.0.1:8000/shopping/"
  }).then(function(res){
    console.log(res.data);
    $scope.items=res.data;
    $scope.data=[
      {"a":"q","b":"p","c":"r"}
    ]
    $scope.records = [
      {
        "Name" : "Alfreds Futterkiste",
        "Country" : "Germany"
      },
      {
        "Name" : "Berglunds snabbköp",
        "Country" : "Sweden"
      },
      {
        "Name" : "Centro comercial Moctezuma",
        "Country" : "Mexico"
      },
      {
        "Name" : "Ernst Handel",
        "Country" : "Austria"
      }
    ]
  })
  
// app.controller("default", function)
})