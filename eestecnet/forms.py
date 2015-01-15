from django.contrib import messages
from django.forms import Form, CharField, Textarea
from django.http import JsonResponse


class AdditionalContextMixin(object):
    additional_context = {}

    def get_context_data(self, **kwargs):
        context = super(AdditionalContextMixin, self).get_context_data(**kwargs)
        context.update(self.additional_context)
        return context


class MassCommunicationForm(Form):
    subject = CharField(max_length=255)
    message = CharField(widget=Textarea)

class DialogFormMixin(object):
    template_name = "forms/dialog_form_with_inlines.html"
    html_id = "dialogform"
    form_id = "dialogformform"
    submit = "Update"
    additional_context = {}
    can_add = False

    def action(self):
        return self.request.path
    def form_invalid(self, form):
        response = super(DialogFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            response.render()
            data = {
                'content': response.content,
            }
            return JsonResponse(data, status=200)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(DialogFormMixin, self).form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             "Update successful. The changes might take a minute to "
                             "become effective due to caching.")
        if self.request.is_ajax():
            data = {}
            return JsonResponse(data, status=200)
        else:
            return response
    def get_context_data(self, **kwargs):
        context = super(DialogFormMixin, self).get_context_data(**kwargs)
        if self.request.is_ajax():
            context['parent'] = "base/prototypes/ajax.html"
        else:
            context['parent'] = self.parent_template
        context['id'] = self.html_id
        context['form_id'] = self.form_id
        context['title'] = self.form_title
        context['submit'] = self.submit
        context['action'] = self.action
        context['can_add'] = self.can_add
        context.update(self.additional_context)
        return context


from django import forms
from django.utils.safestring import mark_safe


class SpanWidget(forms.Widget):
    '''Renders a value wrapped in a <span> tag.

    Requires use of specific form support. (see ReadonlyForm
    or ReadonlyModelForm)
    '''

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<span%s >%s</span>' % (
            forms.util.flatatt(final_attrs), self.display_value))

    def value_from_datadict(self, data, files, name):
        return self.original_value


class SpanField(forms.Field):
    '''A field which renders a value wrapped in a <span> tag.

    Requires use of specific form support. (see ReadonlyForm
    or ReadonlyModelForm)
    '''

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = kwargs.get('widget', SpanWidget)
        super(SpanField, self).__init__(*args, **kwargs)


class Readonly(object):
    '''Base class for ReadonlyForm and ReadonlyModelForm which provides
    the meat of the features described in the docstings for those classes.
    '''

    class NewMeta:
        readonly = tuple()

    def __init__(self, *args, **kwargs):
        super(Readonly, self).__init__(*args, **kwargs)
        readonly = self.NewMeta.readonly
        if not readonly:
            return
        for name, field in self.fields.items():
            if name in readonly:
                field.widget = SpanWidget()
            elif not isinstance(field, SpanField):
                continue
            model_field = self.instance._meta.get_field_by_name(name)[0]
            field.widget.original_value = model_field.value_from_object(self.instance)
            field.widget.display_value = unicode(getattr(self.instance, name))


class ReadonlyForm(Readonly, forms.Form):
    '''A form which provides the ability to specify certain fields as
    readonly, meaning that they will display their value as text wrapped
    with a <span> tag. The user is unable to edit them, and they are
    protected from POST data insertion attacks.

    The recommended usage is to place a NewMeta inner class on the
    form, with a readonly attribute which is a list or tuple of fields,
    similar to the fields and exclude attributes on the Meta inner class.

        class MyForm(ReadonlyForm):
            foo = forms.TextField()
            class NewMeta:
                readonly = ('foo',)
    '''
    pass


class ReadonlyModelForm(Readonly, forms.ModelForm):
    '''A ModelForm which provides the ability to specify certain fields as
    readonly, meaning that they will display their value as text wrapped
    with a <span> tag. The user is unable to edit them, and they are
    protected from POST data insertion attacks.

    The recommended usage is to place a NewMeta inner class on the
    form, with a readonly attribute which is a list or tuple of fields,
    similar to the fields and exclude attributes on the Meta inner class.

        class Foo(models.Model):
            bar = models.CharField(max_length=24)

        class MyForm(ReadonlyModelForm):
            class Meta:
                model = Foo
            class NewMeta:
                readonly = ('bar',)
    '''
    pass
