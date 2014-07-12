$(function () {
    var login = $("dialog.login");
    login.dialog({autoOpen: false, show: {duration: 500}});
    $("#login").click(function () {
        if (login.dialog("isOpen")) {
            login.dialog("close");
        } else {
            login.dialog("open");
        }
    });
    $(".date").datepicker({changeYear: true, yearRange: "-30:-18"});
    $(".datetime").datetimepicker();
});
