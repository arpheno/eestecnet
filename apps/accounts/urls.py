from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

from apps.accounts.views import  AccountViewSet, MembershipViewSet
from apps.events.views import GroupViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

grouprouter = SimpleRouter()
grouprouter.register(r'groups', GroupViewSet)
membershiprouter = SimpleRouter()
membershiprouter.register(r'memberships', MembershipViewSet)


accountrouter = SimpleRouter()
accountrouter.register(r'accounts', AccountViewSet)

