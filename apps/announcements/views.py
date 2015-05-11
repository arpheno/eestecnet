from rest_framework.viewsets import ModelViewSet

from apps.announcements.models import Announcement
from apps.announcements.serializers import AnnouncementSerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


