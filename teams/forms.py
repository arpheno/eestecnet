from django.forms import Form, ModelMultipleChoiceField, ModelForm
from extra_views import InlineFormSet

from account.models import Eestecer
from news.models import Membership
from news.widgets import EESTECEditor
from teams.models import Team, MemberImage
from teams.widgets import MultiSelectWidget


class BoardForm(Form):
    board_members = ModelMultipleChoiceField(queryset=Eestecer.objects.none(),
                                             widget=MultiSelectWidget)

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team')
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['board_members'].queryset = Eestecer.objects.filter(
            membership__team=team)


class DescriptionForm(ModelForm):
    class Meta:
        model = Team
        fields = ('description',)
        widgets = {'description': EESTECEditor(include_jquery=False)}
        #'css': "/static/enet/css/wysiwyg.css"})}


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        exclude = ('board',)


class MembershipInline(InlineFormSet):
    model = Membership
    extra = 0
    form_class = MembershipForm


class MemberImageInline(InlineFormSet):
    model = MemberImage

