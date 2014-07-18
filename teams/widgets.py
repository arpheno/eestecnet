from django import forms
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class MultiSelectWidget(forms.SelectMultiple):
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''

        imgsrc = self.choices.queryset[int(option_value) - 1].profile_picture.url
        return format_html(
            '<option data-img-src=' + imgsrc + ' value="{0}"{1}>{2}</option>',
            option_value,
            selected_html,
            force_text(option_label))

    def render(self, name, value, attrs=None):
        rendered = super(MultiSelectWidget, self).render(name, value, attrs)
        filter = mark_safe(
            '<input type="text" id="personpicker_filter_%(name)s">' % {'name': name})
        predialog = filter + rendered
        postdialog = mark_safe(u'''<div id="personpicker_%(name)s">''' % {
        'name': name}) + predialog + '</div>'
        javascript = mark_safe(u'''<script type="text/javascript">
            $(document).ready(function afterReady() {
                var elem = $('#id_%(name)s');
                elem.imagepicker({"show_label":true});
                $(".image_picker_image").attr({"height":"100px","width":"100px"})
                $(".thumbnail p").hide();
                $("#personpicker_%(name)s").dialog({create:function(){
                    refresh=setInterval(function(){
                        $("#personpicker_%(name)s li").hide();
                        var filt=$('#personpicker_filter_%(name)s').val();
                        $("#personpicker_%(name)s li:contains("+filt+")").show();
                    },500);
                 }});
            $("#personpicker_%(name)s").dialog("option","width",550);
            acsrc= $("#personpicker_%(name)s .thumbnail p").contents();
            ac=[];
            acsrc.each(function(item){ac.push(acsrc[item].data);});
            $("#personpicker_filter_%(name)s").keypress(function(event) {
                if (event.keyCode == 13) {
                    event.preventDefault();
                }
            });
            $("#personpicker_filter_%(name)s").autocomplete({source:ac});
        });
            </script>''' % {'name': name})
        return postdialog + javascript