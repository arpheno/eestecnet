from rest_framework.serializers import ModelSerializer

from apps.prioritylists.models import PriorityList, Priority


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class PriorityListSerializer(ModelSerializer):
    class Meta:
        model = PriorityList
        fields = ('event', 'commitment', 'users')


class PrioritySerializer(ModelSerializer):
    class Meta:
        model = Priority
