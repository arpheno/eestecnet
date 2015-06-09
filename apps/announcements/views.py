from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
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
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class NewsViewSet(AnnouncementViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CareerOfferViewSet(AnnouncementViewSet):
    queryset = CareerOffer.objects.all()
    serializer_class = CareerOfferSerializer