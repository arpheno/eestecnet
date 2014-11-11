from django.forms import ModelForm, Textarea, TextInput, FileField, Form
from extra_views import InlineFormSet

from events.models import Event, EventImage, Transportation
from news.widgets import EESTECEditor


class TransportForm(ModelForm):
    class Meta:
        model = Transportation
        fields = (
            'arrival', 'arrive_by', 'arrival_number', 'departure', 'depart_by',
            'comment')
        widgets = {
            'arrival': TextInput(attrs={'class': 'datetime'}),
            'departure': TextInput(attrs={'class': 'datetime'}),
            'comment': Textarea(attrs={'rows': '1'}),
        }


class UploadEventsForm(Form):
    file = FileField()


class DescriptionForm(ModelForm):
    class Meta:
        model = Event
        fields = ('description',)
        widgets = {'description': EESTECEditor(include_jquery=False)}
        #'css': "/static/enet/css/wysiwyg.css"})}


class EventImageInline(InlineFormSet):
    model = EventImage


