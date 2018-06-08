$(document).ready(function () {
    $('.navbar').addClass('hide');

    $('#signInModal').modal({
        backdrop: false
    });
    $('#signInModal').modal('show');

    $('#signIn').click(function () {
        var data = {
            username: $("#username").val(),
            pwd: $("#password").val()
        };
        $.post("/user_login", data, function (res) {
            if (res['code'] == 0) {
                $('#passwordInfo').addClass('hide');
                window.location.href = "/list";
            } else {
                $('#passwordInfo').removeClass('hide');
            }
        }, "json");
    });
});