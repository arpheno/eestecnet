import string
import random
import logging

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import RequestSite
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.views.generic import UpdateView, DetailView, CreateView, FormView, View, \
    ListView
from django.forms import TextInput
from form_utils.forms import BetterModelForm
from form_utils.widgets import ImageWidget
from mailqueue.models import MailerMessage
from password_reset.utils import get_username

from apps.account.forms import EestecerCreationForm, EestecerPersonalForm
from apps.account.models import Eestecer
from apps.pages.widgets import Grids, Information, AdminOptions
from eestecnet.forms import DialogFormMixin, MassCommunicationForm
from apps.events.models import Event
from apps.news.widgets import EESTECEditor

logger = logging.getLogger(__name__)
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class CapitalizeName(object):
    def get_initial(self):
        initial={}
        user = self.get_object()
        initial['first_name'] =user.first_name.title()
        initial['middle_name'] =user.middle_name.title()
        initial['last_name'] =user.last_name.title()
        initial['second_last_name'] =user.second_last_name.title()
        return initial

def complete(request, ida):
    try:
        user = Eestecer.objects.get(activation_link=ida)
    except:
        logger.info("Someone try to activate their account, but it failed.")
        return redirect('/')
    user.is_active = True
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    logger.info(str(user) + " activated their account.")
    messages.add_message(request, messages.SUCCESS,
                         "Your account is active, please update your profile picture "
                         "and additional info.")
    return redirect('/people/me')


class EestecerProfile(AdminOptions, Information, Grids, DetailView):
    def information(self):
        info = [
            ('Name', self.get_object().name),
            ('Birthday', self.get_object().date_of_birth),
            ('Date Joined', self.get_object().date_joined),
            ('Field of Study', self.get_object().get_field_of_study_display()),
        ]
        if self.get_object().curriculum_vitae:
            info.append(("Curriculum Vitae",
                         "<a href='" + self.get_object().curriculum_vitae.url + "'" +
                         ">Download</a>"))
        return info

    def adminoptions(self):
        if not self.request.user == self.get_object() and not \
                self.request.user.is_superuser:
            return []
        options = []
        options.append(('Change Details', reverse_lazy('userupdate')))
        options.append(('Change Personal Description', reverse_lazy('personalupdate')))
        return options


    def grids(self):
        grids = [
            ("teams/grids/base.html", self.get_object().teams.all(), "LC and Teams"),
        ]
        if self.get_object().events_organized.all():
            grids.append((
            "events/grids/base.html", self.get_object().events_organized.all(),
            "Last Events Organized"))
        if self.get_object().events.all():
            grids.append((
            "events/grids/base.html", self.get_object().events.all(), "Last Events"))
        return grids
    model = Eestecer
    template_name= "account/eestecer_detail.html"


class EestecerUpdateForm(BetterModelForm):
    class Meta:
        model=Eestecer
        fieldsets = [
            ('Name',
             {'fields': ['first_name', 'middle_name', 'last_name', 'second_last_name']}),
            ('Additional Information', {'fields': [
                'gender', 'date_of_birth', 'show_date_of_birth',
                'thumbnail', 'field_of_study', 'curriculum_vitae']}),
            ('Contact Information', {'fields': [
                'hangouts', 'mobile', 'description', 'skype']}),
            ('Event Information', {'fields': [
                'tshirt_size', 'passport_number', 'food_preferences', 'allergies']}),
            ('Administrative Information', {'fields': ['receive_eestec_active']}),
        ]
        widgets = {
            'date_of_birth': TextInput(attrs={'class': 'date'}),
            'description': EESTECEditor(include_jquery=False),
            'thumbnail': ImageWidget(
                template='<span>%(image)s<br />%(input)s</span>'),
        }

class TrainingList(DetailView):
    template_name = "account/training_list.html"
    model = Eestecer

    def get_context_data(self, **kwargs):
        context = super(TrainingList, self).get_context_data(**kwargs)
        context['trainings'] = list(
            Event.objects.filter(organizers=context['object'], category="training"))
        for training in context['trainings']:
            training.name = training.name.split("-" + str(training.start_date))[0]
        return context


class PersonalUpdate(UpdateView):
    form_class = EestecerPersonalForm
    model = Eestecer
    template_name = "account/personalform.html"

    def get_object(self, queryset=None):
        return self.request.user

class EestecerUpdate(CapitalizeName,DialogFormMixin, UpdateView):
    model=Eestecer
    parent_template = "account/eestecer_detail.html"
    form_class = EestecerUpdateForm
    form_title = "Update your personal info"
    additional_context={"appendix":render_to_string("account/password_reset.html")}
    def get_success_url(self):
        return self.get_object().get_absolute_url()

    action = "/people/me"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(EestecerUpdate, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.ERROR,
            'You forgot required fields')
        return super(EestecerUpdate, self).form_invalid(form)

    def form_valid(self, form):
        logger.info(str(self.request.user) + " updated their account information.")
        messages.add_message(
            self.request,
            messages.INFO,
            'Your information has been updated.')
        user=form.save(commit=False)
        user.update_forum()
        return super(EestecerUpdate, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


class EestecerList(Grids, ListView):
    model=Eestecer
    template_name = 'account/all_eestecers.html'

    def grids(self):
        return [
            ("account/grids/base.html", self.get_queryset(), "People in EESTEC"),
        ]

    def get_queryset(self):
        qs = super(EestecerList, self).get_queryset()
        return qs.exclude(thumbnail="")


class EestecerCreate(DialogFormMixin, CreateView):
    model=Eestecer
    form_title = "Almost done!"
    submit = "Sign Up!"
    parent_template = "base/base.html"
    form_class = EestecerCreationForm
    action = "/register/"
    def get_success_url(self):
        return "/"

    def form_valid(self, form):
        user = form.save(commit=False)
        logger.info(str(user) + " registered on the website.")
        user.is_active = False
        user.activation_link = id_generator(30)
        message = MailerMessage()
        context = {
            'site': RequestSite(self.request),
            'user': user,
            'username': get_username(user),
            'secure': self.request.is_secure(),
            "activation_link": user.activation_link
        }
        message.subject = "Registration"
        message.content = render_to_string("account/registration.html", context)
        message.from_address = "noreply@eestec.net"
        message.to_address = user.email
        message.save()
        user.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Registration successful. Please check your email to complete the process.')
        return super(EestecerCreate, self).form_valid(form)


class Login(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        return redirect("/")
    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.INFO,
            'The user you specified does not exist, or the password provided was '
            'incorrect. If you have forgotten your password click <a href="' + reverse(
                "password_reset_recover") + '">  here</a>.'
        )
        return redirect("/")

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.INFO,
            'You\'re now logged in as ' + unicode(form.get_user())
        )
        login(self.request, form.get_user())
        return redirect("/")

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO, 'You\'re now logged out')
        return redirect("/")


class PrivilegedCommunication(DialogFormMixin, FormView):
    parent_template = "base/base.html"
    form_class = MassCommunicationForm
    form_title = "Send a message to all registered users"
    submit = "Send message"
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(PrivilegedCommunication, self).dispatch(request, *args,
                                                                 **kwargs)
        raise PermissionDenied

    def form_valid(self, form):
        logger.info(str(
            self.request.user) + " just sent an email to all privileged members of the EESTEC Community: " +
                    form.cleaned_data['message'])
        message = MailerMessage()
        message.subject = form.cleaned_data['subject']
        message.content = form.cleaned_data['message']
        message.from_address = "noreply@eestec.net"
        message.to_address = "board@eestec.net"
        message.bcc_address = ", ".join(
            user.email for user in Eestecer.objects.filter(groups__name="Local Admins"))
        message.save()
        messages.add_message(
            self.request,
            messages.INFO, "Message will be sent now."
        )
        return redirect("/")


class MassCommunication(DialogFormMixin, FormView):
    parent_template = "base/base.html"
    form_class = MassCommunicationForm
    form_title = "Send a message to all registered users"
    submit = "Send message"
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(MassCommunication, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def form_valid(self, form):
        logger.info(str(
            self.request.user) + " just sent an email to the whole EESTEC Community: " +
                    form.cleaned_data['message'])
        message = MailerMessage()
        message.subject = form.cleaned_data['subject']
        message.content = form.cleaned_data['message']
        message.from_address = "noreply@eestec.net"
        message.to_address = "board@eestec.net"
        message.bcc_address = ", ".join(
            user.email for user in Eestecer.objects.filter(receive_eestec_active=True))
        message.save()
        messages.add_message(
            self.request,
            messages.INFO, "Message will be sent now."
        )
        return redirect("/")
