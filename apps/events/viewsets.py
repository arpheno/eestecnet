from rest_framework import viewsets

from apps.events.models import Event
from apps.events.serializers import EventSerializer
from eestecnet.serializers import AdminMixin


class Events(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.filter(
        category__in=["workshop", "training", "operational", "exchange", "imw"])
    serializer_class = EventSerializer


