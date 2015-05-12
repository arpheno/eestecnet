from rest_framework.fields import HiddenField
from rest_framework.fields import CurrentUserDefault

from rest_framework.serializers import ModelSerializer

from apps.teams.models import BaseTeam, InternationalTeam, Commitment


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
class TeamSerializer(ModelSerializer):
    class Meta:
        model = BaseTeam

    owner = HiddenField(
        default=CurrentUserDefault()
    )
class InternationalTeamSerializer(TeamSerializer):
    class Meta:
        model = InternationalTeam
class CommitmentSerializer(TeamSerializer):
    class Meta:
        model = Commitment




