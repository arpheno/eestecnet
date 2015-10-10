from rest_framework.fields import HiddenField
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.teams.models import BaseTeam, InternationalTeam, Commitment
from common.serializers import ImageSerializer, serializer_factory, LocationSerializer, URLSerializer

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
TEAM_LIST = ["pk", "images", "name", "locations"]
TEAM_PUBLIC = ["pk", "images", "name", "locations",
               "description", "urls", "members"]


def team_serializer_factory(mdl):
    return serializer_factory(
        mdl,
        images=ImageSerializer(many=True, read_only=True),
        locations=LocationSerializer(many=True, read_only=True),
        urls=URLSerializer(many=True, read_only=True),
        owner=HiddenField(default=CurrentUserDefault())
    )


def team_public_serializer_factory(mdl):
    return serializer_factory(
        mdl, fields=TEAM_PUBLIC,
        locations=LocationSerializer(many=True, read_only=True),
        urls=URLSerializer(many=True, read_only=True),
        images=ImageSerializer(many=True, read_only=True)
    )


def team_list_serializer_factory(mdl):
    return serializer_factory(
        mdl, fields=TEAM_LIST,
        locations=LocationSerializer(many=True, read_only=True),
        images=ImageSerializer(many=True, read_only=True)
    )

