from rest_framework_nested import routers

from apps.events.views import GroupViewSet, EventViewSet, TrainingViewSet, \
    ExchangeViewSet, WorkshopViewSet, TravelViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
eventrouter = routers.SimpleRouter()

