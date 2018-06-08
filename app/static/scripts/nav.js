$(document).ready(function () {
    $('#signOut').click(function () {
        $.post("/user_logout", function (res) {
            if (res['code'] == 0) {
                $('#aUsername').html('<b class="caret"></b>');
                window.location.href = "/";
            }
        });
    });

    $.post("/is_login", function (res) {
        if (res['code'] == 0) {
            $('#aUsername').html(res['data'] + '<b class="caret"></b>');
            $('body').removeClass('hide');
        } else {
            window.location.href = "/";
        }
    }, "json");

});