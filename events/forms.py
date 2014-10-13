from django.forms import ModelForm
from extra_views import InlineFormSet

from events.models import Event, EventImage
from news.widgets import EESTECEditor


class DescriptionForm(ModelForm):
    class Meta:
        model = Event
        fields = ('description',)
        widgets = {'description': EESTECEditor(include_jquery=False)}
        #'css': "/static/enet/css/wysiwyg.css"})}


class EventImageInline(InlineFormSet):
    model = EventImage


