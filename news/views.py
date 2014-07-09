from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from news.models import Entry


class home(ListView):
    model = Entry
    template_name = 'enet/home.html'
