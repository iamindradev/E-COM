var app = angular.module("app", ["ngCookies"]);
app.controller("loginn", function ($scope, $http, $cookies) {
  $scope.login = function () {
    var value = {
      username: $scope.username,
      password: $scope.password,
    };
    console.log(value);
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/login/",
      data: value,
    }).then(function (res) {
      console.log(res.data);
      if (typeof res.data == "number") {
        swal({
          text: "LOGGED IN SUCCESFULLY",
        });
        console.log(res.headers());
        // $cookies.put("customer_id", res.data);
        localStorage.setItem("id", res.data);
        window.location.href = "http://127.0.0.1:5500/frontend/home.html";
      } else if (res.data == "wrong password") {
        swal({
          text: "WRONG PASSWORD",
        });
        console.log(res.headers());
      } else if (
        res.data == "you haven't registered yet or wrong mail/contact"
      ) {
        swal({
          text: "YOU HAVEN'T REGISTERED YET OR WRONG MAIL/CONTACT",
        });
        console.log(res.headers());
      }
    });
  };
});
