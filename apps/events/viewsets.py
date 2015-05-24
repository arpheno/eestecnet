from rest_framework import viewsets
from apps.account.models import Eestecer
from apps.account.serializers import LegacyAccountSerializer

from apps.events.models import Event
from apps.events.serializers import EventSerializer, LegacyEventSerializer
from apps.teams.models import Team
from apps.teams.serializers import LegacyTeamSerializer
from eestecnet.serializers import AdminMixin


class lEvents(viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lEvents, self).dispatch(request,*args,**kwargs)
    queryset = Event.objects.exclude(category="recruitment")
    serializer_class = LegacyEventSerializer
class lAccounts(viewsets.ModelViewSet):
    queryset = Eestecer.objects.all()
    serializer_class = LegacyAccountSerializer
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lAccounts, self).dispatch(request,*args,**kwargs)
class lTeams(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = LegacyTeamSerializer
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lTeams, self).dispatch(request,*args,**kwargs)





