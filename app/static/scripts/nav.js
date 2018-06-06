$(document).ready(function(){
    $('#signIn').click(function(){
        var data = {
            username: $("#username").val(),
            password: $("#password").val()
        };
        $.post("/signIn", data ,function(res){
            console.log(res);
            $('#navUsername').val('abc');
        });
    });

    $('#signOut').click(function(){
        var data = {
            username: $("#navUsername").val()
        };
        $.post("/signOut", data ,function(res){
            console.log(res);
        });
    });
});