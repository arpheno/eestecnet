from rest_framework import viewsets
from rest_framework.filters import DjangoObjectPermissionsFilter

from apps.events.models import Event, Application, Participation
from apps.events.serializers import EventSerializer, ParticipationSerializer, \
    IncomingSerializer
from eestecnet import permissions
from eestecnet.serializers import AdminMixin


class Participants(viewsets.ReadOnlyModelViewSet):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()

    def list(self, request, event_pk=None):
        self.queryset = self.queryset.filter(target__pk=event_pk)
        return super(Participants, self).list(request)


class Incoming(viewsets.ReadOnlyModelViewSet):
    queryset = Application.objects.all()
    filter_backends = [DjangoObjectPermissionsFilter]
    permission_classes = [permissions.CustomObjectPermissions]
    serializer_class = IncomingSerializer

    def list(self, request, event_pk=None):
        self.queryset = self.queryset.filter(target__pk=event_pk)
        return super(Incoming, self).list(request)
class Events(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


