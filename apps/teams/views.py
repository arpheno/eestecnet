from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


# Create your views here.
from django.views.generic import ListView, FormView, UpdateView, View, TemplateView, \
    DetailView
from extra_views import UpdateWithInlinesView, ModelFormSetView
from apps.pages.widgets import Information
from apps.pages.widgets import Grids
from apps.pages.widgets import AdminOptions
from eestecnet.forms import DialogFormMixin
from eestecnet.views import NeverCacheMixin
from apps.events.admin import get_own_members
from apps.events.models import Event, Application
from apps.teams.forms import MembershipInline, MemberImageInline, DescriptionForm, \
    BoardForm, \
    ApplicationInline, TeamImageForm, OutgoingApplicationForm
from apps.teams.models import Team, Board


class TeamMixin(NeverCacheMixin, View):
    parent_template = "teams/team_detail.html"
    form_title = "Please fill in the form"

    def dispatch(self, request, *args, **kwargs):
        subject = Team.objects.get(slug=kwargs['slug'])
        if request.user in subject.privileged() or request.user.is_superuser:
            return super(TeamMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        if Team.objects.get(slug=self.kwargs['slug']).is_lc():
            return reverse_lazy("cities:detail", kwargs=self.kwargs)
        return reverse_lazy("teams:detail", kwargs=self.kwargs)


class TeamList(Grids, ListView):
    model = Team
    def grids(self):
        return [
            ("teams/grids/base.html", self.get_queryset(), "Cities of EESTEC"),
            ]
    def get_queryset(self):
        return Team.objects.filter(category='team')



class TeamDetail(Information, Grids, AdminOptions, DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data(**kwargs)
        user = self.request.user
        object = self.get_object()
        context[
            'may_apply'] = user.is_authenticated and user not in object.users.all() \
                           and user not in object.pending_applications()
        context['recruitment'] = object.event_set.get(category="recruitment")
        return context

    def information(self):
        return [
            ('Committee Name', self.get_object().name),
            ('Founded in', self.get_object().founded),
            ('Website', self.get_object().website),
            ('Number of Members', self.get_object().member_count()),
        ]

    def grids(self):
        return [
            ("events/grids/base.html",
             self.get_object().event_set.exclude(category="recruitment"), "Last Events"),
            ("account/grids/base.html", self.get_object().organizers(), "Board"),
            ("account/grids/base.html", self.get_object().members(), "Members"),
            ("account/grids/base.html", self.get_object().alumni(), "Alumni"),
        ]

    def adminoptions(self):
        if not self.request.user in self.get_object().privileged() and not \
                self.request.user.is_superuser:
            return []
        return [
            ("Outgoing", reverse_lazy(self.request.resolver_match.app_name+':outgoing',kwargs=self.kwargs)),
            ('Change Board', self.get_object().get_absolute_url() + "board"),
            ('Change Details', self.get_object().get_absolute_url() + "details"),
            ('Manage Members', self.get_object().get_absolute_url() + "members"),
            ('Manage Images', self.get_object().get_absolute_url() + "images"),
            ('Outgoing Applications', self.get_object().get_absolute_url() + "outgoing"),
            ('Incoming Applications', self.get_object().get_absolute_url() + "applications"),
        ]


class History(TemplateView):
    template_name = "enet/history.html"


class Governance(TemplateView):
    template_name = "teams/governance.html"

    def get_context_data(self, **kwargs):
        context = super(Governance, self).get_context_data(**kwargs)
        try:
            context["current_board"] = Board.objects.order_by('-year')[0]
        except:
            pass
        return context


class CommitmentList(Grids,ListView):
    model = Team
    def grids(self):
        return [
            ("teams/grids/base.html", self.get_queryset(), "Cities of EESTEC"),
        ]
    def get_queryset(self):
        return Team.objects.filter(category__in=["lc", "jlc", "observer"]).order_by('name')


class ManageMembers(TeamMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Team
    fields = ()
    inlines = [MembershipInline]


class OutgoingApplications(TeamMixin, DialogFormMixin, ModelFormSetView):
    model = Application
    template_name = "forms/dialog_modelformset.html"
    extra = 0
    form_class = OutgoingApplicationForm

    def get_queryset(self):
        return super(OutgoingApplications, self).get_queryset().filter(
            applicant__in=get_own_members(self.request))


class TeamApplications(TeamMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    fields = ()
    inlines = [ApplicationInline]
    form_title = "These people want to join!"

    def get_context_data(self, **kwargs):
        context = super(TeamApplications, self).get_context_data(**kwargs)
        context['object'] = context['object'].organizing_committee.first()
        return context

    def get_object(self, queryset=None):
        return Event.objects.get(category='recruitment',
                                 organizing_committee__slug=self.kwargs['slug'])


class TeamImages(TeamMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Team
    fields = ('thumbnail',)
    inlines = [MemberImageInline]
    form_class = TeamImageForm


class ChangeDetails(TeamMixin, DialogFormMixin, UpdateView):
    model = Team
    fields = ('name', 'website', 'address', 'founded', 'facebook')


class ChangeDescription(TeamMixin, DialogFormMixin, UpdateView):
    form_class = DescriptionForm
    model = Team
    template_name = "teams/description.html"


class SelectBoard(TeamMixin, DialogFormMixin, FormView):
    form_class = BoardForm

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
            membership.organizers = False
            membership.save()

        for user in form.cleaned_data['board_members']:
            mmbrship = user.membership_set.get(team=team)
            mmbrship.organizers = True
            mmbrship.save()
        return super(SelectBoard, self).form_valid(form)