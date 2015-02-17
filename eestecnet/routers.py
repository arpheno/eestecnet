from rest_framework import routers

from apps.account.viewsets import People, GroupViewset
from apps.events.viewsets import Events
from apps.teams.viewsets import Cities


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cities', Cities)
router.register(r'people', People)
router.register(r'events', Events)
router.register(r'groups', GroupViewset)
