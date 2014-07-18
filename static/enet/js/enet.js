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
function PersonPicker(wrapper) {
    var self = this;
    this.wrapper = wrapper;
    this.imgpicker = this.wrapper.find("select");
    this.imgpicker.imagepicker({"show_label": true});
    this.wrapper.find("img").attr({"height": "100px", "width": "100px"});
    this.filter = this.wrapper.find('.filter');
    this.labels = this.wrapper.find(".thumbnail p");
    this.imgs = this.wrapper.find("li");
    this.labels.hide();
    this.wrapper.dialog();
    refresh = setInterval(function () {
        self.imgs.hide();
        self.imgs.filter(":contains('" + self.filter.val() + "')").show();
    }, 500);
    this.wrapper.dialog("option", "width", 550);
    var acsrc = this.labels.contents();
    this.ac = [];
    acsrc.each(function (item) {
        self.ac.push(acsrc[item].data);
    });
    this.filter.keypress(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    });
    this.filter.autocomplete({source: self.ac});
}