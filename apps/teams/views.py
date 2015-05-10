from rest_framework.viewsets import ModelViewSet

from apps.teams.models import BaseTeam, Commitment, InternationalTeam
from apps.teams.serializers import TeamSerializer, CommitmentSerializer, \
    InternationalTeamSerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class BaseTeamViewSet(ModelViewSet):
    queryset = BaseTeam.objects.all()
    serializer_class = TeamSerializer


class CommitmentViewSet(ModelViewSet):
    queryset = Commitment.objects.all()
    serializer_class = CommitmentSerializer


class InternationalTeamViewSet(ModelViewSet):
    queryset = InternationalTeam.objects.all()
    serializer_class = InternationalTeamSerializer
