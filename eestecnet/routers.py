from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from apps.account.viewsets import People, GroupViewset
from apps.events.viewsets import Events, Incoming, Participants
from apps.news.viewsets import News
from apps.teams.viewsets import Cities, TeamMembers, Outgoing
from eestecnet.serializers import Permissions


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cities', Cities)
cities_router = NestedSimpleRouter(router, r'cities', lookup='city')

cities_router.register(r'outgoing', Outgoing)
cities_router.register(r'members', TeamMembers)
router.register(r'people', People)
router.register(r'events', Events)
events_router = NestedSimpleRouter(router, r'events', lookup='event')
events_router.register(r'incoming', Incoming)
events_router.register(r'members', Participants)
router.register(r'people', People)
router.register(r'news', News)
router.register(r'groups', GroupViewset)
router.register(r'permissions', Permissions)
