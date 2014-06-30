from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from events.models import Event
from members.models import Member

class MemberDetail(DetailView):
    model=Member
    def get_object(self, queryset=None):

        return Member.objects.get(name__iexact=self.kwargs['slug'].replace("_"," "))

class TeamList(ListView):
    model = Member
    def get_queryset(self):
        return Member.objects.filter(type='team')

class CommitmentList(ListView):
    model = Member
    def get_queryset(self):
        return Member.objects.filter(type__in=["lc","jlc","observer"])
def create_eestec(self,request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    if not request.user.is_superuser():
        return HttpResponse(html)


