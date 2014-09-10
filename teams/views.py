from django.core.urlresolvers import reverse


# Create your views here.
from django.views.generic import ListView, FormView, UpdateView, View, TemplateView
from extra_views import UpdateWithInlinesView, InlineFormSet
from events.models import Event, Application
from teams.forms import MembershipInline, MemberImageInline, DescriptionForm, BoardForm
from teams.models import Team, Board


class TeamMixin(View):
    def get_success_url(self):
        if Team.objects.get(slug=self.kwargs['slug']).is_lc():
            return reverse("cities:detail", kwargs=self.kwargs)
        return reverse("teams:detail", kwargs=self.kwargs)


class TeamList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type='team')


class Governance(TemplateView):
    template_name = "teams/governance.html"

    def get_context_data(self, **kwargs):
        context = super(Governance, self).get_context_data(**kwargs)
        try:
            context["current_board"] = Board.objects.order_by('-year')[0]
        except:
            pass
        return context


class CommitmentList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type__in=["lc", "jlc", "observer"])


class ManageMembers(TeamMixin, UpdateWithInlinesView):
    model = Team
    template_name = 'teams/manage_members_form.html'
    fields = ()
    inlines = [MembershipInline]


class ApplicationInline(InlineFormSet):
    model = Application
    extra = 0


class TeamApplications(TeamMixin, UpdateWithInlinesView):
    model = Event
    template_name = 'teams/team_applications_form.html'
    fields = ()
    inlines = [ApplicationInline]

    def get_context_data(self, **kwargs):
        context = super(TeamApplications, self).get_context_data(**kwargs)
        context['object'] = context['object'].organizing_committee.first()
        return context

    def get_object(self, queryset=None):
        return Event.objects.get(category='recruitment',
                                 organizing_committee__slug=self.kwargs['slug'])


class TeamImages(TeamMixin, UpdateWithInlinesView):
    model = Team
    template_name = 'teams/team_images_form.html'
    fields = ('thumbnail',)
    inlines = [MemberImageInline]

    def get_context_data(self, **kwargs):
        context = super(TeamImages, self).get_context_data(**kwargs)
        return context


class ChangeDetails(TeamMixin, UpdateView):
    template_name = 'teams/change_details_form.html'
    model = Team
    fields = ('name', 'website', 'address', 'founded', 'facebook')


class ChangeDescription(TeamMixin, UpdateView):
    template_name = 'teams/description_form.html'
    form_class = DescriptionForm
    model = Team


class SelectBoard(TeamMixin, FormView):
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