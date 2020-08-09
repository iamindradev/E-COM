var app = angular.module("app" ,[]);
app.controller("login", function($scope, $http){
    $scope.log= function(){
        
    }
    
    $scope.register=function(){
        
    }
    $scope.submit= function(){
        $http=({
            method:"POST",
            url:"http://127.0.0.1:8000/mail_to_user",
            data:{
                email:$scope.mail
            }
        }).then(function(res){
            console.log(res.data);
        })
    }
})