from django.forms import ModelForm


# Create your views here.
from django.views.generic import ListView, DetailView, FormView
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


class BoardForm(ModelForm):
    class Meta:
        model = Team
        fields = (('users'),)
        widgets = {'users': MultiSelectWidget()}


class appoint_new_board(FormView):
    form_class = BoardForm
    template_name = 'teams/board_form.html'

