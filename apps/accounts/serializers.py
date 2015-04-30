from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Group


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
