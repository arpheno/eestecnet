from rest_framework.fields import HiddenField, CurrentUserDefault

from rest_framework.serializers import ModelSerializer

from apps.accounts.serializers import GroupSerializer, UnprivilegedAccountSerializer
from apps.events.models import Travel
from common.serializers import ReportSerializer, ImageSerializer, URLSerializer, serializer_factory, LocationSerializer

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

EVENT_PUBLIC = ["pk", "images", "name", "organizing_committee"
    , "description", "urls", "start_date"
    , "end_date", "deadline", "participants", "locations"]
EVENT_LIST = ["pk", "images", "name", "organizing_committee", "locations"]


def event_public_serializer_factory(mdl):
    myserializer = serializer_factory(
        mdl, fields=EVENT_PUBLIC,
        images=ImageSerializer(many=True, read_only=True),
        participants=UnprivilegedAccountSerializer(many=True, read_only=True),
        locations=LocationSerializer(many=True, read_only=True),
        urls=URLSerializer(many=True, read_only=True))
    return myserializer


def event_serializer_factory(mdl):
    myserializer = serializer_factory(
        mdl,
        owner=HiddenField(default=CurrentUserDefault()),
        reports=ReportSerializer(many=True, read_only=True),
        images=ImageSerializer(many=True, read_only=True),
        locations=LocationSerializer(many=True, read_only=True),
        urls=URLSerializer(many=True, read_only=True),
        group_set=GroupSerializer(many=True, read_only=True))
    return myserializer


def event_list_serializer_factory(mdl):
    myserializer = serializer_factory(
        mdl, fields=EVENT_LIST,
        images=ImageSerializer(many=True, read_only=True),
        locations=LocationSerializer(many=True, read_only=True))
    return myserializer


class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
