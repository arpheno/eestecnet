import string
import random

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.views.generic import UpdateView, DetailView, CreateView, FormView, View, \
    ListView
from django.forms import TextInput
from form_utils.forms import BetterModelForm
from form_utils.widgets import ImageWidget

from account.forms import EestecerCreationForm
from account.models import Eestecer
from events.models import Event
from news.widgets import EESTECEditor


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def complete(request, ida):
    try:
        user = Eestecer.objects.get(activation_link=ida)
    except:
        return redirect('/')
    user.is_active = True
    user.save()
    #login(request, user)
    messages.add_message(request, messages.SUCCESS,
                         "Your account is active, please update your profile picture "
                         "and additional info.")
    return redirect('/')


class EestecerProfile(DetailView):
    model = Eestecer
    template_name= "account/eestecer_detail.html"


class EestecerUpdateForm(BetterModelForm):
    class Meta:
        model=Eestecer
        fields = (
        'first_name', 'middle_name', 'last_name', 'second_last_name', 'date_of_birth',
        'field_of_study', 'curriculum_vitae',
        'profile_picture','gender','tshirt_size','passport_number','food_preferences','allergies',
        'skype', 'hangouts', 'mobile', 'personal')
        widgets = {
            'date_of_birth': TextInput(attrs={'class': 'date'}),
            'personal': EESTECEditor(include_jquery=False),
            'profile_picture': ImageWidget(
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


class EestecerUpdate(UpdateView):
    model=Eestecer
    form_class = EestecerUpdateForm
    success_url = "/people/me"
    template_name = 'account/eestecer_form.html'

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.ERROR,
            'You forgot required fields')
        return super(EestecerUpdate, self).form_invalid(form)

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.INFO,
            'Your information has been updated.')
        return super(EestecerUpdate, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
class EestecerList(ListView):
    model=Eestecer
    template_name = 'account/all_eestecers.html'
class EestecerCreate(CreateView):
    model=Eestecer
    form_class = EestecerCreationForm
    template_name = 'account/eestecer_create.html'
    success_url = '/'
    def get_success_url(self):
        return "/"

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.INFO,
            'Registration successful. Please check your email to complete the process.')
        return super(EestecerCreate, self).form_valid(form)


class Login(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm

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
