$(function () {
    $(".date").datepicker({changeYear: true, yearRange: "-35:-18"});
    $(".datetime").datetimepicker();
    $("a[href^=#]").click(function (e) {
    });
    $("#feedbackbutton").click(function () {
        $("#feedbackarea").load("/pages/feedback/");
    });
    $("#feedbackform form ").submit(function () {


        var url = "/pages/feedback/"; // the script where you handle the form input.

        $.ajax({
            type: "POST",
            url: url,
            data: $("#feedbackform form").serialize(), // serializes the form's elements.
            success: function (data) {
                alert("Thank you for your feedback, we appreciate it.");
                $("#feedbackform form input[type=text], textarea").val("");
            }
        });
        $("#feedbackform").dialog("close");
        return false; // avoid to execute the actual submit of the form.
    });
    $("#registerbutton").click(function () {
        $("#dialog").load("/register/");
        return false;
    });

});
function PersonDialog(wrapper) {
    var self = this;
    this.wrapper = wrapper;
    this.filter = this.wrapper.find('.filter');
    this.labels = this.wrapper.find(".thumbnail p");
    this.imgs = this.wrapper.find("img").parent().parent();
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
