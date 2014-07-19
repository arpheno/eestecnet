from django.core.urlresolvers import reverse
from django.forms import Form, ModelMultipleChoiceField


# Create your views here.
from django.views.generic import ListView, FormView
from account.models import Eestecer
from teams.models import Team
from teams.widgets import MultiSelectWidget



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


class SelectBoard(FormView):
    form_class = BoardForm
    template_name = 'teams/board_form.html'

    def get_context_data(self, **kwargs):
        context = super(SelectBoard, self).get_context_data(**kwargs)
        context['object'] = Team.objects.get(slug=self.kwargs['slug'])
        return context

    def get_form_kwargs(self):
        kwargs = super(SelectBoard, self).get_form_kwargs()
        kwargs['team'] = Team.objects.get(slug=self.kwargs['slug'])
        return kwargs

    def get_success_url(self):
        return reverse("city", kwargs=self.kwargs)

    def form_valid(self, form):
        team = Team.objects.get(slug=self.kwargs['slug'])
        for membership in team.membership_set.all():
            membership.board = False
            membership.save()

        for user in form.cleaned_data['board_members']:
            mmbrship = user.membership_set.get(team=team)
            mmbrship.board = True
            mmbrship.save()
        return super(SelectBoard, self).form_valid(form)