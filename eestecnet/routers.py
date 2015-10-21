from rest_framework import routers

from apps.account.viewsets import People, GroupViewset
from apps.events.viewsets import Events
from apps.news.viewsets import News, Memberships
from apps.teams.viewsets import Cities
from eestecnet.serializers import Permissions


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cities', Cities)
router.register(r'people', People)
router.register(r'events', Events)
router.register(r'news', News)
router.register(r'memberships', Memberships)
router.register(r'groups', GroupViewset)
router.register(r'permissions', Permissions)
