from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from events.models import Event
from members.models import Member


class TeamList(ListView):
    model = Member
    def get_queryset(self):
        return Member.objects.filter(type='team')

class CommitmentList(ListView):
    model = Member
    def get_queryset(self):
        return Member.objects.filter(type__in=["lc","jlc","observer"])
