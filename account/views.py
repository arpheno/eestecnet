from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, DetailView, CreateView, FormView, View, \
    ListView
from django.forms import ModelForm, TextInput
import string
import random
from account.forms import EestecerCreationForm
from account.models import Eestecer


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def complete(request, ida):
    try:
        user = Eestecer.objects.get(registration=ida)
    except:
        return redirect('/')
    user.is_active = True
    user.save()
    return redirect('/')


class EestecerProfile(DetailView):
    model = Eestecer
    template_name= "account/eestecer_detail.html"
class EestecerUpdateForm(ModelForm):
    class Meta:
        model=Eestecer
        fields=('first_name','middle_name','last_name','second_last_name','date_of_birth',
        'profile_picture','gender','tshirt_size','passport_number','food_preferences','allergies',
        'skype','hangouts','mobile',)
        widgets = {
            'date_of_birth': TextInput(attrs={'class': 'date'}),
            'departure': TextInput(attrs={'class': 'date'}),
            }

class EestecerUpdate(UpdateView):
    model=Eestecer
    form_class = EestecerUpdateForm
    success_url = "/people/me"
    template_name = 'account/eestecer_form.html'

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
class Login(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm
    def form_valid(self, form):
        login(self.request,form.get_user())
        return redirect("/")
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
