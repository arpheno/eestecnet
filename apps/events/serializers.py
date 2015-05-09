from rest_framework.serializers import ModelSerializer

from apps.events.models import BaseEvent, Exchange, Training, Workshop


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class BaseEventSerializer(ModelSerializer):
    class Meta:
        model = BaseEvent


class ExchangeSerializer(BaseEventSerializer):
    class Meta:
        model = Exchange


class TrainingSerializer(ModelSerializer):
    class Meta:
        model = Training


class WorkshopSerializer(ModelSerializer):
    class Meta:
        model = Workshop
