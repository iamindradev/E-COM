var id = localStorage.getItem("id");
var orderid = localStorage.getItem("orderid");
var app = angular.module("app", ["ngRoute"]);
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
      .when("/orders", {
        templateUrl: "orders.html",
      })
      .when("/wishlist", {
        templateUrl: "wishlist.html",
      })
      .when("/ordercnf", {
        templateUrl: "ordercnf.html",
        controller: "order",
      });
  },
]);
app.controller("home", function ($scope, $http) {
  $http({
    method: "GET",
    url: "http://127.0.0.1:8000/shopping/",
  }).then(function (res) {
    console.log(res.data);
    $scope.items = res.data;
  });
  $scope.makeorder = function (item) {
    var value = {
      product_id: item.id,
      buyer_id: id,
    };
    console.log(value);
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/shopping/makeorder/",
      data: value,
    }).then(function (res) {
      console.log(res.data);
    });
  };

  // app.controller("default", function)
});

app.controller("order", function ($scope, $http) {
  $http({
    method: "POST",
    url: "http://127.0.0.1:8000/shopping/product/",
    data: {
      id: id,
    },
  }).then(function (res) {
    console.log(res.data);
    $scope.items = res.data;
  });
  $scope.makepayment = function () {
    var value = {
      orderid: $scope.orderid,
      custid: $scope.custid,
      amount: $scope.amount,
    };
    localStorage.setItem("orderid", orderid);
    console.log(value);
    $http({
      method: "POST",
      url: "http://127.0.0.1:8000/payment/",
      data: value,
    }).then(function (res) {
      console.log(res.data);
      window.location.href = "http://127.0.0.1:5500/frontend/payment.html";
    });
  };
});
// app.controller("payment", function ($scope, $http) {
//   $http({
//     method: "POST",
//     url: "http://127.0.0.1:8000/payment/paydata/",
//     data: {
//       orderid: orderid,
//     },
//   }).then(function (res) {
//     console.log(res.data);
//     $scope.items = res.data;
//     $scope.orderid = orderid;
//   });
// });
