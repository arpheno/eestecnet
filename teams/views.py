from django.forms import Form, ModelMultipleChoiceField


# Create your views here.
from django.views.generic import ListView, DetailView, FormView
from account.models import Eestecer
from teams.models import Team
from teams.widgets import MultiSelectWidget


class MemberDetail(DetailView):
    model = Team

    def get_object(self, queryset=None):
        return Team.objects.get(name__iexact=self.kwargs['slug'].replace("_", " "))


class TeamList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type='team')


class CommitmentList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type__in=["lc", "jlc", "observer"])


class BoardForm(Form):
    board_members = ModelMultipleChoiceField(queryset=Eestecer.objects.none(),
                                             widget=MultiSelectWidget)

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team')
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['board_members'].queryset = Eestecer.objects.filter(
            membership__team=team)


class appoint_new_board(FormView):
    form_class = BoardForm
    template_name = 'teams/board_form.html'

    def get_form_kwargs(self):
        kwargs = super(appoint_new_board, self).get_form_kwargs()
        kwargs['team'] = Team.objects.get(slug=self.kwargs['slug'])
        return kwargs

    def get_success_url(self):
        return "/cities/" + self.kwargs['slug'] + "/"

    def form_valid(self, form):
        team = Team.objects.get(slug=self.kwargs['slug'])
        for membership in team.membership_set.all():
            membership.board = False
            membership.save()

        for user in form.cleaned_data['board_members']:
            mmbrship = user.membership_set.get(team=team)
            mmbrship.board = True
            mmbrship.save()
        return super(appoint_new_board, self).form_valid(form)