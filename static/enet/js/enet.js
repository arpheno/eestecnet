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
function PersonDialog(wrapper) {
    var self = this;
    this.wrapper = wrapper;
    this.filter = this.wrapper.find('.filter');
    this.labels = this.wrapper.find(".thumbnail p");
    this.imgs = this.wrapper.find("li");
    this.labels.hide();
    this.chosen = function () {
        return this.imgs.find(".selected img");
    }

    //Create the dialog window
    this.wrapper.dialog({
        appendTo: self.wrapper.parent(),
        create: self.timer = refresh = setInterval(function () {
            console.log("running")
            self.imgs.hide();
            self.imgs.filter(":contains('" + self.filter.val() + "')").show();
        }, 500),
        close: function () {
            clearInterval(self.timer);
        }
    });
    this.wrapper.dialog("option", "width", 550);

    //Initiate the autocomplete plugin
    var acsrc = this.labels.contents();
    this.ac = [];
    acsrc.each(function (item) {
        self.ac.push(acsrc[item].data);
    });
    this.filter.autocomplete({source: self.ac});

    // Prevent Enter Keypresses from submitting the form
    this.filter.keypress(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    });
}