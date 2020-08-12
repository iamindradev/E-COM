var app = angular.module("app", []);
app.controller("login", function ($scope, $http) {
  $scope.submit = function (){
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/register/",
      data: {
        'fname':$scope.fname,
        'lname':$scope.lname,
        'email': $scope.mail,
        'password':$scope.password
      }
    }).then(function (res) {
      console.log(res.data)
    })
    }
  })

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