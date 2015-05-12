from rest_framework.serializers import ModelSerializer

from apps.announcements.models import Announcement, News, CareerOffer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News


class CareerOfferSerializer(ModelSerializer):
    class Meta:
        model = CareerOffer