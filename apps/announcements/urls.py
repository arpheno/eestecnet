from rest_framework_nested import routers

from apps.announcements.views import AnnouncementViewSet, NewsViewSet, CareerOfferViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

announcementrouter = routers.SimpleRouter()

announcementrouter.register(r'announcements', AnnouncementViewSet)
announcementrouter.register(r'news', NewsViewSet)
announcementrouter.register(r'careers', CareerOfferViewSet)




