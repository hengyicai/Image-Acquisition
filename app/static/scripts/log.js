$(document).ready(function () {
    $('#navLog').addClass('active');

    $.post("/tail_log", function (res) {
        var logs = res['msg'].split('\n');
        for (var i = 0; i < logs.length; i++) {
            $("#content").append("<option>" + logs[i] + "</option>");
        }
    });
});