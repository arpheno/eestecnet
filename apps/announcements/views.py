from rest_framework.viewsets import ModelViewSet

from apps.announcements.models import Announcement, News, CareerOffer
from apps.announcements.serializers import AnnouncementSerializer, \
    CareerOfferSerializer, \
    NewsSerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CareerOfferViewSet(ModelViewSet):
    queryset = CareerOffer.objects.all()
    serializer_class = CareerOfferSerializer