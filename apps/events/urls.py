from rest_framework_nested import routers

from apps.events.views import GroupViewSet, EventViewSet, TrainingViewSet, \
    ExchangeViewSet, WorkshopViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

eventrouter = routers.SimpleRouter()
eventrouter.register(r'events', EventViewSet)
eventrouter.register(r'training-sessions', TrainingViewSet)
eventrouter.register(r'exchanges', ExchangeViewSet)
eventrouter.register(r'workshops', WorkshopViewSet)

package_router = routers.NestedSimpleRouter(eventrouter, r'events', lookup='event')


package_router.register(r'groups', GroupViewSet)
