var app = angular.module("app", ["ngRoute"]);
app.config([
  "$routeProvider",
  function ($routeProvider) {
    $routeProvider
      .when("/", {
        templateUrl: "email.html",
      })
      .when("/mobile", {
        templateUrl: "mobile.html",
      });
  },
]);
app.controller("login", function ($scope, $http) {
  $scope.submit = function () { 
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/register/",
      data: {
        'fname': $scope.fname,
        'lname': $scope.lname,
        'identity': document.getElementById('identity').value,
        'password': $scope.password,
        'typ': document.getElementById('typ').value
      },
    }).then(function (res) {
      console.log(res.data);
    });
  };

  $scope.login = function () {
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/register/",
      data: {
        username: $scope.username,
        password: $scope.pasword,
      },
    }).then(function (res) {
      console.log(res.data);
    });
  };
});

//   $scope.submit=function(){
//     $http({
//         method:"POST",
//         url:"http://6ce91d4cb417.ngrok.io/query/new/",
//         data:{
//             'lib_id':id,
//             'query':$scope.query ,
//         }
//     }).then(function(res){
//         console.log(res.data)
//     })
// }
