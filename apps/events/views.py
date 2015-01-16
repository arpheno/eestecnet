import csv
import logging
import random
import datetime

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.files import File
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import widgets
from django.forms.models import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    FormView, \
    DeleteView
from extra_views import UpdateWithInlinesView, CreateWithInlinesView
from form_utils.widgets import ImageWidget

from apps.news.models import Membership
from apps.pages.widgets import Grids, Information, AdminOptions
from eestecnet.forms import DialogFormMixin
from apps.events.forms import DescriptionForm, EventImageInline, TransportForm, \
    UploadEventsForm, EventMixin, EventUpdateForm, EventCreationForm
from apps.events.models import Event, Application, Participation
from apps.teams.forms import ApplicationInline, ParticipationInline
from apps.teams.models import Team


logger = logging.getLogger(__name__)


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


class InternationalEvents(AdminOptions, Grids, ListView):
    model = Event

    def adminoptions(self):
        if not self.request.user.is_superuser and not Membership.objects.filter(
                privileged=True, user=self.request.user):
            return []
        options = [
            ('Create New Event', reverse_lazy('create_event')),
            ('New Questionaire', reverse_lazy('newquestionset')),
        ]
        return options

    def grids(self):
        return [
            ("events/grids/base.html", self.get_events()['active_list'],
             "Events Open for Application"),
            ("events/grids/base.html", self.get_events()['pending_list'],
             "Events in Progress"),
            ("events/grids/base.html", self.get_events()['over_list'], "Past Events"),
        ]

    def get_events(self):
        events = self.get_queryset().filter(scope="international")
        eventlist = {}
        eventlist['active_list'] = []
        eventlist['pending_list'] = []
        eventlist['over_list'] = []
        for event in events:
            if event.deadline and event.deadline > timezone.now():
                eventlist['active_list'].append(event)
            if event.deadline and event.deadline < timezone.now() and event.end_date > \
                    timezone.now().date():
                eventlist['pending_list'].append(event)
            if event.deadline and event.end_date and event.end_date < timezone.now(

            ).date():
                eventlist['over_list'].append(event)
        return eventlist


def confirm_event(request, slug):
    try:
        pa = Participation.objects.get(target__slug=slug, participant=request.user)
    except:
        return redirect(reverse('event', kwargs={'slug': slug}))
    pa.confirmed = True
    pa.confirmation = 0
    pa.save()
    logger.info(
        str(pa.participant) + " just confirmed their participation to " + str(pa.target))
    return redirect(reverse('event', kwargs={'slug': slug}))


class EventDetail(AdminOptions, Information, Grids, DetailView):
    model = Event
    template_name = "events/event_detail.html"

    def adminoptions(self):
        options = []
        if self.request.user in self.get_object().members.all():
            options.append(
                ('Feedback', reverse_lazy('answer_feedback', kwargs=self.kwargs)))
        if not self.request.user.is_superuser and not Membership.objects.filter(
                team=self.get_object(), privileged=True, user=self.request.user):
            return options
        options.append(
            ('Change Details', reverse_lazy('eventchangedetails', kwargs=self.kwargs)))
        options.append(
            ('Manage Images', reverse_lazy('eventimages', kwargs=self.kwargs)))
        options.append(
            ('Participants', reverse_lazy('eventparticipation', kwargs=self.kwargs)))

        if self.get_object().application_set.all():
            options.append(('Incoming Applications',
                            reverse_lazy('eventapplications', kwargs=self.kwargs)))
        return options

    def information(self):
        event = self.get_object()
        date = str(event.start_date)
        if event.end_date:
            date += str(event.end_date)
        information = [
            ('Event Name', self.get_object().name),
            ('Organizing Committee', self.get_object().OC()),
            ('Date', date),
            ('Number of Members', self.get_object().member_count()),
        ]
        if event.deadline:
            information.append(('Deadline', event.deadline))
        if event.max_participants:
            information.append(('Maximum Participants', event.max_participants))
        return information

    def grids(self):
        event = self.get_object()
        return [
            ("teams/grids/base.html", event.organizing_committee.all(),
             "Organizing Committee"),
            ("account/grids/base.html", event.organizers.all(), "Organizers"),
            ("account/grids/base.html", event.members.all(), "Participants"),
        ]

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
    protected = 1
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
    protected = 1
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
    protected = 1
    model = Application
    form_class = modelform_factory(Application, fields=["letter"])
    submit = "Apply"

    def get_context_data(self, **kwargs):
        context = super(ApplyToEvent, self).get_context_data(**kwargs)
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            if not self.request.user.teams.all():
                messages.add_message(
                    self.request,
                    messages.ERROR,
                    'We are sorry. You have to be registered with a EESTEC Committment '
                    'to apply for EESTEC events.')
                return redirect("/")
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
                logger.info(
                    str(self.request.user) + " just tried applying to to " + str(
                        application.target) + " but failed because they have no "
                                              "committment")
                return redirect(self.get_success_url())

        application.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for your application. You will be notified upon acceptance.')
        logger.info(
            str(self.request.user) + " just applied to " + str(application.target))
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
        if not self.request.user.tshirt_size or not self.request.user.thumbnail:
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
    template_name = "events/description.html"


class EventImages(EventMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    form_class = modelform_factory(Event, fields=('thumbnail',),
                                   widgets={'thumbnail': ImageWidget()})
    inlines = [EventImageInline]


class ExportApplications(EventMixin, DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        return self.download_application_details(self.get_applications())

    def get_applications(self):
        return Application.objects.filter(target=self.get_object())

    def download_application_details(self, queryset):
        import xlwt

        response = HttpResponse(content_type='application/ms-excel')
        response[
            'Content-Disposition'] = 'attachment; filename=' + self.get_object().slug \
                                     + 'Application Details.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Incoming Applications")

        row_num = 0

        columns = [
            (u"Full Name", 8000),
            (u"LC", 3000),
            (u"Email", 3000),
            (u"gender", 3000),
            (u"T Shirt Size", 6000),
            (u"Birthday", 6000),
            (u"Allergies", 3000),
            (u"Food Preferences", 4000),
            (u"Mobile Phone", 4000),
            (u"Motivational Letter", 10000),
            (u"Profile Picture", 4000),
            (u"Curriculum Vitae", 4000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1

        for pax in queryset:
            row_num += 1
            thumbnail = ""
            cv = ""
            if pax.applicant.thumbnail:
                thumbnail = "https://eestec.net" + pax.applicant.thumbnail.url
            if pax.applicant.curriculum_vitae:
                cv = "https://eestec.net" + pax.applicant.curriculum_vitae.url
            row = [
                pax.applicant.get_full_name(),
                ", ".join(str(person) for person in pax.applicant.lc()),
                pax.applicant.email,
                pax.applicant.gender,
                pax.applicant.tshirt_size,
                pax.applicant.date_of_birth,
                pax.applicant.allergies,
                pax.applicant.food_preferences,
                pax.applicant.mobile,
                pax.letter,
                thumbnail,
                cv,
            ]

            for col_num in xrange(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


class ExportFeedback(EventMixin, DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        return self.download_feedback()

    def get_participants(self):
        return Participation.objects.filter(target=self.get_object())

    def download_feedback(self):
        import xlwt

        response = HttpResponse(content_type='application/ms-excel')
        response[
            'Content-Disposition'] = 'attachment; filename=' + self.get_object().slug \
                                     + ' Feedback.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        sheet = 0
        for pax in self.get_participants():
            row_num = 0
            ws = wb.add_sheet("Feedback #" + str(sheet))
            columns = [(u"Question", 7000), (u"Answer", 10000)]
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            for col_num in xrange(len(columns)):
                ws.write(row_num, col_num, columns[col_num][0], font_style)
                # set column width
                ws.col(col_num).width = columns[col_num][1]
            font_style = xlwt.XFStyle()
            font_style.alignment.wrap = 1
            for answer in pax.feedback.answer_set.all():
                row_num += 1
                row = [answer.q.q, answer.a]
                for col_num in xrange(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
            sheet += 1
        wb.save(response)
        return response


class ExportParticipants(EventMixin, DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        return self.download_participants_details(self.get_participants())

    def get_participants(self):
        return Participation.objects.filter(target=self.get_object())

    def download_participants_details(self, queryset):
        import xlwt

        response = HttpResponse(content_type='application/ms-excel')
        response[
            'Content-Disposition'] = 'attachment; filename=' + self.get_object().slug \
                                     + 'Participants Details.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Participants Details")
        row_num = 0

        columns = [
            (u"Full Name", 8000),
            (u"LC", 3000),
            (u"Email", 3000),
            (u"gender", 3000),
            (u"T Shirt Size", 6000),
            (u"Birthday", 6000),
            (u"Allergies", 3000),
            (u"Food Preferences", 4000),
            (u"Mobile Phone", 4000),
            (u"Profile Picture", 4000),
            (u"Curriculum Vitae", 4000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1

        for pax in queryset:
            row_num += 1
            thumbnail = ""
            cv = ""
            if pax.participant.thumbnail:
                thumbnail = "https://eestec.net" + pax.participant.thumbnail.url
            if pax.participant.curriculum_vitae:
                cv = "https://eestec.net" + pax.participant.curriculum_vitae.url
            row = [
                pax.participant.get_full_name(),
                ", ".join(str(person) for person in pax.participant.lc()),
                pax.participant.email,
                pax.participant.gender,
                pax.participant.tshirt_size,
                pax.participant.date_of_birth,
                pax.participant.allergies,
                pax.participant.food_preferences,
                pax.participant.mobile,
                thumbnail,
                cv,
            ]

            for col_num in xrange(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        ws = wb.add_sheet("Transportation Details")

        row_num = 0

        columns = [
            (u"Full Name", 8000),
            (u"Arrival Date and Time", 6000),
            (u"Arrival By", 3000),
            (u"Arrival Number", 4000),
            (u"Departure Date and Time", 6000),
            (u"Depart By", 3000),
            (u"Comment", 10000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1

        for pax in queryset:
            if pax.transportation:
                row_num += 1
                row = [
                    pax.participant.get_full_name(),
                    str(pax.transportation.arrival),
                    pax.transportation.arrive_by,
                    pax.transportation.arrival_number,
                    str(pax.transportation.departure),
                    pax.transportation.depart_by,
                ]
                for col_num in xrange(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


class IncomingApplications(EventMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    fields = ()
    inlines = [ApplicationInline]
    form_title = "These people want to participate in the event!"


class Participations(EventMixin, DialogFormMixin, UpdateWithInlinesView):
    model = Event
    fields = ()

    inlines = [ParticipationInline]
    form_title = "These people want to participate in the event!"


class CreateEvent(DialogFormMixin, CreateWithInlinesView):
    model = Event
    form_class = EventCreationForm
    form_title = "Please fill in this form"
    form_id = "createeventform"
    inlines = [EventImageInline]
    parent_template = "events/event_list.html"
    protected = 0
    additional_context = {"appendix": """ <script type="text/javascript">
        $(function () {
            $("input[type=submit]").button();
        });
    </script>"""}
    submit = "Create Event"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('events.add_event'):
            raise PermissionDenied
        return super(CreateEvent, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateEvent, self).get_context_data(**kwargs)
        assert (context["form"])
        return context

    def get_success_url(self):
        return reverse_lazy("events")

    def get_form_kwargs(self):
        kwargs = super(CreateEvent, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['teams'] = self.request.user.teams_administered()
        return kwargs




