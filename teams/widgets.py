from django import forms
from django.template.loader import render_to_string
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
        eestecer = self.choices.queryset.get(id=option_value)
        base = render_to_string('widgets/option.html', {'object': eestecer})
        return format_html(
            base,
            option_value,
            selected_html,
            force_text(option_label))

    def render(self, name, value, attrs=None):
        rendered = super(MultiSelectWidget, self).render(name, value, attrs)
        result = render_to_string(
            'widgets/personpicker.html',
            {'name': name, 'widget': rendered}
        )
        return result