from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.contrib.auth.models import Group
from django.forms import ModelForm
import json
import string
import random
from django.http import HttpResponse
from django.core.mail import send_mail
from account.models import Eestecer


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def new(request):
    username = request.POST['username']
    password = request.POST['password']
    response_data = {}
    try:
        user = Eestecer.objects.create_user(email=username,password=password)
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
        user = Eestecer.objects.get(registration=ida)
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
    user = authenticate(email=username, password=password)
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
