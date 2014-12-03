from django.contrib import admin
from django import forms
from suit_redactor.widgets import RedactorWidget

from pages.models import Page, Stub




# Register your models here.
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en', 'iframe': 'true',
                                                      'css': "/static/enet/css/wysiwyg"
                                                             ".css"}),
        }


class PageAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    form = PageForm


admin.site.register(Page, PageAdmin)
admin.site.register(Stub)
