from rest_framework.viewsets import ModelViewSet

from apps.events.models import BaseEvent
from apps.events.serializers import EventSerializer


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = BaseEvent.objects.all()
    serializer_class = EventSerializer