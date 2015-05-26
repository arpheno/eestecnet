from rest_framework.viewsets import ModelViewSet

from apps.account.models import Eestecer
from apps.conversion.serializers import LegacyEventSerializer, LegacyAccountSerializer, \
    LegacyTeamSerializer, LegacyEntrySerializer
from apps.events.models import Event
from apps.news.models import Entry
from apps.teams.models import Team


class Events(ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(Events, self).dispatch(request, *args, **kwargs)

    queryset = Event.objects.exclude(category="recruitment")
    serializer_class = LegacyEventSerializer


class Accounts(ModelViewSet):
    queryset = Eestecer.objects.all()
    serializer_class = LegacyAccountSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(Accounts, self).dispatch(request, *args, **kwargs)


class Teams(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = LegacyTeamSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(Teams, self).dispatch(request, *args, **kwargs)


class Entries(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = LegacyEntrySerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(Entries, self).dispatch(request, *args, **kwargs)




