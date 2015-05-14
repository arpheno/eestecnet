from rest_framework_nested import routers

from apps.events.views import GroupViewSet, EventViewSet, TrainingViewSet, \
    ExchangeViewSet, WorkshopViewSet, TravelViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
eventrouter = routers.SimpleRouter()
eventrouter.register(r'events', EventViewSet)
eventrouter.register(r'training-sessions', TrainingViewSet)
eventrouter.register(r'exchanges', ExchangeViewSet)
eventrouter.register(r'workshops', WorkshopViewSet)
eventrouter.register(r'travel', TravelViewSet)

package_router = routers.NestedSimpleRouter(eventrouter, r'events', lookup='event')


package_router.register(r'groups', GroupViewSet)
