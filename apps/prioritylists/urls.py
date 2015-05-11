from rest_framework_nested import routers

from apps.prioritylists.views import PriorityListViewSet, PriorityViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

prioritylistrouter = routers.SimpleRouter()
prioritylistrouter.register(r'prioritylists', PriorityListViewSet)
prioritylistrouter.register(r'priorities', PriorityViewSet)

