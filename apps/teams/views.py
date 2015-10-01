from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.events.serializers import event_public_serializer_factory
from apps.teams.models import BaseTeam, Commitment, InternationalTeam
from apps.teams.serializers import  team_serializer_factory
from common.permissions import can_add, can_change

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


class BaseTeamViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = BaseTeam.objects.all()

    def get_serializer_class(self):
        if self.serializer_class:
            return self.serializer_class
        if can_add(self.request.user, self.model):
            return team_serializer_factory(self.model)
        if can_change(self.request.user, self.get_object()):
            return team_serializer_factory(self.model)
        return event_public_serializer_factory(self.model)

        def list(self, request, *args, **kwargs):
            self.serializer_class = event_list_serializer_factory(self.model)
            return super(EventViewSet, self).list(request, *args, **kwargs)


class CommitmentViewSet(BaseTeamViewSet):
    queryset = Commitment.objects.all()
    model = Commitment

class InternationalTeamViewSet(BaseTeamViewSet):
    queryset = InternationalTeam.objects.all()
    model = InternationalTeam
