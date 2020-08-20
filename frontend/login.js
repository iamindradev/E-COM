var app = angular.module ("app", []);
app.controller("loginn" ,function($scope, $http){
    $scope.login= function(){
        var value ={
            'username':$scope.username,
            'password':$scope.password
        }
        $http({
            method:"POST",
            url:"http://127.0.0.1:8000/login/",
            data:value
        }).then(function(res){
            console.log(res.data)
            if (res.data="logged in successfully"){
                swal({
                    text:"LOGGED IN SUCCESFULLY"
                })
                window.location.href="http://127.0.0.1:5500/frontend/home.html";

            }
            else if(res.data="wrong password") {
                swal({
                    text:"WRONG PASSWORD"
                })}
            else if(res.data="you haven't registered yet or wrong mail/contact"){
                swal({
                    text:"YOU HAVEN'T REGISTERED YET OR WRONG MAIL/CONTACT"
                })}
            else{
                swal({
                    text:"SERVER ERROR!!"
                })
            }
            
        })
    }

})