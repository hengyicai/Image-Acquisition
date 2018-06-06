$(document).ready(function(){
    $('#signIn').click(function(){
        var data = {
            username: $("#username").val(),
            pwd: $("#password").val()
        };
        $.post("/user_login", data ,function(res){
            if(res['code'] == 0){
                $('#aUsername').html($('#username').val() + '<b class="caret"></b>');
                $('#navSignIn').addClass('hide');
                $('#navUser').removeClass('hide');
                $('#signInModal').modal('hide');
                $('#passwordInfo').addClass('hide');
            }else{
                $('#passwordInfo').removeClass('hide');
            }
        },"json");
    });

    $('#signOut').click(function(){
        $.post("/user_logout" ,function(res){
            if(res['code'] == 0){
                $('#aUsername').html('<b class="caret"></b>');
                $('#navSignIn').removeClass('hide');
                $('#navUser').addClass('hide');
            }
        });
    });

});