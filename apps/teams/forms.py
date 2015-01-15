from django.forms import Form, ModelMultipleChoiceField, ModelForm
from extra_views import InlineFormSet
from form_utils.forms import BetterModelForm
from form_utils.widgets import ImageWidget

from apps.account.models import Eestecer
from eestecnet.forms import ReadonlyModelForm
from apps.events.models import Application, Participation
from apps.news.models import Membership
from apps.news.widgets import EESTECEditor
from apps.teams.models import Team, MemberImage
from apps.teams.widgets import MultiSelectWidget


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
        # 'css': "/static/enet/css/wysiwyg.css"})}


class OutgoingApplicationForm(ReadonlyModelForm):
    class Meta:
        model = Application
        fields = ('applicant', 'target', 'letter', 'priority')

    class NewMeta:
        readonly = ('applicant', 'target', 'letter')

class MembershipForm(ReadonlyModelForm):
    class Meta:
        model = Membership
        fields = ('user','board', 'privileged', 'alumni')

    class NewMeta:
        readonly = ('user')
    def email(self):
        return self.instance.user.email
class MembershipInline(InlineFormSet):
    model = Membership
    extra = 0
    form_class = MembershipForm


class ApplicationForm(ReadonlyModelForm):
    class Meta:
        model = Application
        fields = ('applicant', 'letter', 'priority', 'accepted')

    class NewMeta:
        readonly = ('applicant', 'letter', 'priority' )


class ParticipationForm(ReadonlyModelForm):
    class Meta:
        model = Participation
        fields = ('participant', 'target')


class ApplicationInline(InlineFormSet):
    model = Application
    extra = 0
    form_class = ApplicationForm


class ParticipationInline(InlineFormSet):
    model = Participation
    extra = 20
    form_class = ParticipationForm

class MemberImageForm(BetterModelForm):
    class Meta:
        model = MemberImage
        widgets = {'image': ImageWidget()}


class MemberImageInline(InlineFormSet):
    model = MemberImage
    form_class = MemberImageForm


class TeamImageForm(BetterModelForm):
    class Meta:
        model = Team
        fields = ('thumbnail',)
        widgets = {'thumbnail': ImageWidget()}
