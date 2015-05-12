from rest_framework.fields import HiddenField
from rest_framework.fields import CurrentUserDefault

from rest_framework.serializers import ModelSerializer

from apps.announcements.models import Announcement, News, CareerOffer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement

    owner = HiddenField(
        default=CurrentUserDefault()
    )


class NewsSerializer(AnnouncementSerializer):
    class Meta:
        model = News


class CareerOfferSerializer(AnnouncementSerializer):
    class Meta:
        model = CareerOffer