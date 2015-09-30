from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.accounts.serializers import GroupSerializer, UnprivilegedAccountSerializer
from apps.events.models import BaseEvent, Exchange, Training, Workshop, Travel
from common.serializers import ReportSerializer, ImageSerializer, URLSerializer

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

EVENT_PUBLIC = ["pk","images","name","description","urls","start_date","end_date","deadline","participants"]
EVENT_LIST = ["pk","images","name"]

class Detail(ModelSerializer):
    class Meta:
        model = BaseEvent

    owner = HiddenField(
        default=CurrentUserDefault()
    )
    reports = ReportSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    group_set = GroupSerializer(many=True, read_only=True)


class DetailPublic(ModelSerializer):
    class Meta:
        model = BaseEvent
        fields = EVENT_PUBLIC
    images = ImageSerializer(many=True, read_only=True)
    participants = UnprivilegedAccountSerializer(many=True,read_only=True)
    urls = URLSerializer(many=True,read_only=True)


class ExchangeSerializer(Detail):
    class Meta:
        model = Exchange


class TrainingSerializer(Detail):
    class Meta:
        model = Training


class WorkshopSerializer(Detail):
    class Meta:
        model = Workshop


class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
