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
    
     var value={
      'fname': document.getElementById('fname').value,
      'lname': document.getElementById('lname').value,
      'identity': document.getElementById('identity').value,
      'password': document.getElementById('password').value,
      'typ': document.getElementById('typ').value
      // 'fname':$scope.fname,
      // 'lname':$scope.lname,
      // 'identity':$scope.identity,
      // 'password':$scope.password,
      // 'typ':$scope.type
      //   ,
     }
    console.log(value)

    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/register/",
      data:value 
    }).then(function (res) {
      console.log(res.data)
      if (res.data=="user exists"){
        swal({
          text: "YOU'VE ALREADY REGISTERED PLEASE LOGIN.",
        });
      }
      else if (res.data =="user created with mail"){
        swal({
          text: "REGISTERED SUCESSFULLY PLEASE CHECK YOUR MAIL",
        });
      
      }
      else{
        window.location.href="http://127.0.0.1:5500/frontend/confirm.html#!/"
        swal({
          text:"REGISTERED SUCESSFULLY PLEASE CHECK MESSAGE FOR OTP"
        });
        
      }
    });
  };

  $scope.confirmotp= function () {
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/confirm/",
      data: {
        'otp':$scope.otp
      },
    }).then(function (res) {
      console.log(res.data);
      if(res.data=="verified"){
        window.location.href="http://127.0.0.1:5500/frontend/home.html";
        swal({
          text:"CONFIRMED. LOGGED IN SUCCESSFULLY"
        });
      }
      else{
        window.location.href="http://127.0.0.1:5500/frontend/register.html#!/" ;
          swal({
            text:"REGISTER AGAIN"
          });
        }
      
    });
  };
});
 


