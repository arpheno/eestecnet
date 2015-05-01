from rest_framework_nested import routers
from apps.events.views import GroupViewSet, EventViewSet


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

eventrouter = routers.SimpleRouter()
eventrouter.register(r'events', EventViewSet)

package_router = routers.NestedSimpleRouter(eventrouter, r'events', lookup='event')


package_router.register(r'groups', GroupViewSet)