from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.accounts.models import Group
from apps.accounts.serializers import GroupSerializer
from apps.events.models import BaseEvent, Training, Exchange, Workshop, Travel
from apps.events.serializers import Detail, TrainingSerializer, \
    ExchangeSerializer, WorkshopSerializer, TravelSerializer, DetailPublic

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class EventViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = BaseEvent.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return Detail
        return DetailPublic


class TrainingViewSet(EventViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class ExchangeViewSet(EventViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class WorkshopViewSet(EventViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TravelViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer