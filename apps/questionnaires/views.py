from rest_framework.viewsets import ModelViewSet

from apps.accounts.models import Group
from apps.accounts.serializers import GroupSerializer
from apps.events.models import BaseEvent
from apps.events.serializers import EventSerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = BaseEvent.objects.all()
    serializer_class = EventSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, event_pk=None):
        self.queryset = self.queryset.filter(applicable=event_pk)
        return super(GroupViewSet, self).list(request)

    def retrieve(self, request, pk=None, event_pk=None):
        if event_pk:
            self.object = self.queryset.get(pk=pk, applicable=event_pk)
        else:
            self.object = self.queryset.get(pk=pk)
        return super(GroupViewSet, self).retrieve(request)
