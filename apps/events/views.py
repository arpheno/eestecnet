from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.accounts.models import Group
from apps.accounts.serializers import GroupSerializer
from apps.events.models import BaseEvent, Training, Exchange, Workshop, Travel
from apps.events.serializers import Detail, TrainingSerializer, \
    ExchangeSerializer, WorkshopSerializer, TravelSerializer, DetailPublic, EventListSerializer

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def can_change(user, obj):
    return user.has_perm('change_' + obj._meta.object_name.lower(), obj)
def can_add(user, cls):
    return user.has_perm('add' + cls._meta.model_name)


class EventViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    model = BaseEvent
    queryset = BaseEvent.objects.all()
    def get_queryset(self):
        return self.model.objects.all()
    def get_serializer_class(self):
        if self.serializer_class:
            return self.serializer_class
        if can_add(self.request.user,self.model):
            return Detail
        if can_change(self.request.user, self.get_object()):
            return Detail
        return DetailPublic

    def list(self, request, *args, **kwargs):
        self.serializer_class = EventListSerializer
        return super(EventViewSet, self).list(request, *args, **kwargs)


class TrainingViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class ExchangeViewSet(ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class WorkshopViewSet(ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TravelViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
