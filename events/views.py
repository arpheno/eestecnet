import csv
import random
import datetime

from django.contrib import messages
from django.core.files import File
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.forms.models import modelform_factory
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    FormView, \
    DeleteView
from extra_views import UpdateWithInlinesView
from form_utils.widgets import ImageWidget
from eestecnet.forms import DialogFormMixin
from events.forms import DescriptionForm, EventImageInline, TransportForm, \
    UploadEventsForm, EventMixin, EventUpdateForm
from events.models import Event, Application, Participation
from teams.forms import ApplicationInline
from teams.models import Team


class HTML5Input(widgets.Input):
    def __init__(self, type, attrs):
        self.input_type = type
        super(HTML5Input, self).__init__(attrs)


def featuredevent():
    try:
        random_idx = random.randint(0, Event.objects.filter(scope="international",
                                                            start_date__gt=datetime
                                                            .date.today()).exclude(
            category='recruitment').count() - 1)
        random_event = Event.objects.filter(
            scope="international", start_date__gt=datetime.date.today()).exclude(
            category='recruitment')[random_idx]
    except:
        random_event = Event.objects.filter(category="workshop").latest('start_date')
    return random_event


class AddEvents(FormView):
    form_class = UploadEventsForm
    template_name = "events/add_events.html"
    success_url = "/"

    def form_valid(self, form):
        self.handle_events(self.request.FILES['file'])
        return super(AddEvents, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddEvents, self).get_context_data(**kwargs)
        context['object'] = self.request.user
        return context

    def handle_events(self, f):
        eventreader = csv.reader(f)
        for event in eventreader:
            messages.success(self.request, " ".join([item for item in event]))
            try:
                t_oc = Team.objects.get(name=event[4])
            except:
                messages.success(self.request, "Cant find team " + event[4])
            t_oc = Team.objects.get(name=event[4])
            new_event = Event.objects.create(
                name=event[0] + "tempobject" + str(random.randint(1, 50000)),
                deadline=event[1],
                start_date=event[2],
                end_date=event[3],
                category=event[5],
                description=event[6],
                summary=event[7],
                scope=event[8],
                max_participants=event[9],
            )
            new_event.save()
            new_event.organizers.add(self.request.user)
            new_event.organizing_committee.add(t_oc)
            if new_event.category == "training":
                if "ommunication" in new_event.name:
                    thumbname = "communication-skills.jpg"
                elif "motional" in new_event.name:
                    thumbname = "emotional-intelligence.jpg"
                elif "eedback" in new_event.name:
                    thumbname = "feedback.jpg"
                elif "resentation" in new_event.name:
                    thumbname = "presentation-skills.jpg"
                elif "rganizational" in new_event.name:
                    thumbname = "organizational-management.jpg"
                elif "eadership" in new_event.name:
                    thumbname = "leadership.jpg"
                elif "roject" in new_event.name:
                    thumbname = "project-management.jpg"
                elif "ime" in new_event.name and "anagement" in new_event.name:
                    thumbname = "time-management.jpg"
                elif "eambuilding" in new_event.name:
                    thumbname = "teambuilding.JPG"
                elif "acilitation" in new_event.name:
                    thumbname = "facilitation.jpg"
                elif "ynamics" in new_event.name:
                    thumbname = "group-dynamics.jpg"
                elif "ody" in new_event.name and "anguage" in new_event.name:
                    thumbname = "body-language.jpg"
                else:
                    thumbname = "trtlogo.png"
                with open('eestecnet/training/' + thumbname, 'rb') as doc_file:
                    new_event.thumbnail.save("thumbname.jpg", File(doc_file), save=True)
                randstring = ""
                try:
                    Event.objects.get(name=event[0] + "-" + str(new_event.start_date))
                    randstring = str(random.randint(1, 500))
                except:
                    pass
                new_event.name = event[0] + "-" + str(new_event.start_date) + randstring
            else:
                new_event.name = event[0]
            new_event.save()


class InternationalEvents(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InternationalEvents, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        events = context['object_list'].filter(scope="international")
        context['active_list'] = []
        context['pending_list'] = []
        context['over_list'] = []
        for event in events:
            try:
                if event.deadline:
                    if event.deadline > timezone.now():
                        context['active_list'].append(event)
                    if event.deadline < timezone.now() and event.end_date > timezone \
                            .now() \
                            .date():
                        context['pending_list'].append(event)
                if event.end_date < timezone.now().date():
                    context['over_list'].append(event)
            except:
                pass
        return context


def confirm_event(request, slug):
    try:
        pa = Participation.objects.get(target__slug=slug, participant=request.user)
    except:
        return redirect(reverse('event', kwargs={'slug': slug}))
    pa.confirmed = True
    pa.confirmation = 0
    pa.save()
    return redirect(reverse('event', kwargs={'slug': slug}))


class EventDetail(DetailView):
    model = Event
    template_name = "events/event_detail.html"

    def get_context_data(self, **kwargs):

        context = super(EventDetail, self).get_context_data(**kwargs)
        if self.get_object().deadline:
            context['applicable'] = timezone.now() < self.get_object().deadline
        else:
            context['applicable'] = timezone.now().date() <= self.get_object().start_date
        try:
            context['participation'] = Participation.objects.get(
                target__slug=self.kwargs['slug'], participant=self.request.user)
        except:
            context['participation'] = None
        return context


class DeleteApplication(DialogFormMixin, DeleteView):
    protected = 0
    model = Application

    def get_object(self, queryset=None):
        event = Event.objects.get(slug=self.kwargs['slug'])
        return Application.objects.get(applicant=self.request.user, target=event)

    def get_context_data(self, **kwargs):
        context = super(DeleteApplication, self).get_context_data(**kwargs)
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect(reverse('event', kwargs=self.kwargs))


class EditApplication(EventMixin, DialogFormMixin, UpdateView):
    protected = 0
    model = Application
    form_class = modelform_factory(Application, fields=["letter"])

    def get_object(self, queryset=None):
        event = Event.objects.get(slug=self.kwargs['slug'])
        return Application.objects.get(applicant=self.request.user, target=event)

    def get_context_data(self, **kwargs):
        context = super(EditApplication, self).get_context_data(**kwargs)
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context


class ApplyToEvent(EventMixin, DialogFormMixin, CreateView):
    protected = 0
    model = Application
    form_class = modelform_factory(Application, fields=["letter"])
    submit = "Apply"

    def get_context_data(self, **kwargs):
        context = super(ApplyToEvent, self).get_context_data(**kwargs)
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            Application.objects.get(
                applicant=request.user,
                target=Event.objects.get(slug=self.kwargs['slug']))
            return redirect(self.get_success_url())
        except:
            return super(ApplyToEvent, self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('event', kwargs=self.kwargs)

    def form_valid(self, form):
        application = form.save(commit=False)
        application.applicant = self.request.user
        application.target = Event.objects.get(slug=self.kwargs['slug'])
        if application.target.deadline:
            if timezone.now() > application.target.deadline:
                messages.add_message(
                    self.request,
                    messages.INFO,
                    'We are sorry. The deadline for this event has passed.')
                return redirect(self.get_success_url())

        application.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for your application. You will be notified upon acceptance.')
        return redirect(self.get_success_url())


class UpdateTransport(EventMixin, DialogFormMixin, UpdateView):
    protected = 0
    form_class = TransportForm

    def get_object(self, queryset=None):
        return Participation.objects.get(applicant=self.request.user,
                                         target=Event.objects.get(
                                             slug=self.kwargs['slug'])).transportation


class FillInTransport(EventMixin, DialogFormMixin, CreateView):
    protected = 0
    form_class = TransportForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FillInTransport, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        if not self.request.user.tshirt_size or not self.request.user.profile_picture:
            return redirect(reverse('event', kwargs=self.kwargs))
        pax = get_object_or_404(Participation, participant=self.request.user,
                                target__slug=self.kwargs['slug'])
        trans = form.save()
        pax.transportation = trans
        pax.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for filling in your transportation details.')
        return redirect(reverse('event', kwargs=self.kwargs))


class ChangeDetails(EventMixin, DialogFormMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm


class ChangeDescription(EventMixin, DialogFormMixin, UpdateView):
    form_class = DescriptionForm
    model = Event


class EventImages(EventMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    form_class = modelform_factory(Event, fields=('thumbnail',),
                                   widgets={'thumbnail': ImageWidget()})
    inlines = [EventImageInline]


class IncomingApplications(EventMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    fields = ()
    inlines = [ApplicationInline]
    form_title = "These people want to participate in the event!"

