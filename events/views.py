from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from events.models import Event


class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event