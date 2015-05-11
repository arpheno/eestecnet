from rest_framework.serializers import ModelSerializer

from apps.announcements.models import Announcement


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement


