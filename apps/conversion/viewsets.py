from rest_framework.viewsets import ModelViewSet

from apps.account.models import Eestecer
from apps.conversion.serializers import LegacyEventSerializer, LegacyAccountSerializer, \
    LegacyTeamSerializer
from apps.events.models import Event
from apps.teams.models import Team


class lEvents(ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lEvents, self).dispatch(request, *args, **kwargs)

    queryset = Event.objects.exclude(category="recruitment")
    serializer_class = LegacyEventSerializer


class lAccounts(ModelViewSet):
    queryset = Eestecer.objects.all()
    serializer_class = LegacyAccountSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lAccounts, self).dispatch(request, *args, **kwargs)


class lTeams(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = LegacyTeamSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(lTeams, self).dispatch(request, *args, **kwargs)




