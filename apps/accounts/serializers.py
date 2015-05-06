from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Group, Account, Participation


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account

class ParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation
