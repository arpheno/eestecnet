from rest_framework.serializers import ModelSerializer

from apps.events.models import BaseEvent


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class EventSerializer(ModelSerializer):
    class Meta:
        model = BaseEvent
