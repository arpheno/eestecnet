from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
import json
import string
import random
from django.http import HttpResponse
from django.core.mail import send_mail


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def new(request):
    username = request.POST['username']
    password = request.POST['password']
    response_data = {}
    try:
        user = User.objects.create_user(username, username, password)
        user.registration = id_generator(30)
        user.save()
        response_data['status'] = 'success'
    except:
        response_data['status'] = 'failure'
        response_data = json.dumps(response_data)
        return HttpResponse(response_data, content_type="application/json")
    response_data = json.dumps(response_data)
    return HttpResponse(response_data, content_type="application/json")


def complete(request, ida):
    try:
        user = User.objects.get(registration=ida)
    except:
        return redirect('/')
    user.is_active = True
    user.save()
    return redirect('/')


def out(request):
    logout(request)
    return redirect('/')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    data = {}
    if user is not None:
        if user.is_active:
            login(request, user)
            if user.is_staff:
                data['staff'] = True
            else:
                data['staff'] = False
            data['status'] = 'success'
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")
        else:
            data['status'] = 'inactive'
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        data['status'] = 'invalid'
        return HttpResponse(json.dumps(data), content_type="application/json")


class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'lc',
                  'trainings_delivered',
                  'profile_picture',
                  'born_on',
                  'join_date',
                  'languages',
                  'preferred_topics',
                  'contact', ]
        labels = {'lc': 'Local Committee',
                  'born_on': 'Date of Birth',
                  'join_date': 'Member of eestec since',
                  'languages': 'Which languages do you speak?',
                  'preferred_topics': 'What are your favourite trainings?',
                  'contact': 'What are the best ways to contact you?'}


    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')


class UserProfile(UpdateView):
    form_class = AccountForm
    template_name = 'account/profile.html'

    def post(self, request, **kwargs):
        instance = User.objects.get(username=self.request.user)
        form = AccountForm(request.POST,request.FILES, instance=instance)
        form.save()
        return redirect('/')

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        return self.request.user
