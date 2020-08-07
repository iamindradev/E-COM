var app = angular.module("login" ,[]);
app.controller("login", function($scope, $http)){
    $scope.log= function(){
        
    }
    
    $scope.register=function(){
        
    }
    $scope.submit= function(){
        $http=({
            method:"POST",
            url:""
        })
    }
}