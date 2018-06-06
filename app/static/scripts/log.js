$(document).ready(function(){
    $('#navLog').addClass('active');

    $.post("/readLog" ,function(res){
        console.log(res);
        $("#content").append("<option>124234242</option>");
    });
});