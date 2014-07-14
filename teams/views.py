from datetime import datetime

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
from django.views.generic import ListView, DetailView
from gmapi.forms.widgets import GoogleMap
from teams.models import Team


class MemberDetail(DetailView):
    model = Team

    def get_object(self, queryset=None):
        return Team.objects.get(name__iexact=self.kwargs['slug'].replace("_", " "))


class TeamList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type='team')


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))
class CommitmentList(ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(type__in=["lc", "jlc", "observer"])


def create_eestec(self,request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    if not request.user.is_superuser():
        return HttpResponse(html)


def emap(request):
    context={}
    return render_to_response('enet/maps.html')
