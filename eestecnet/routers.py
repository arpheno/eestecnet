from rest_framework import routers

from apps.account.viewsets import People
from apps.teams.viewsets import Cities


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cities', Cities)
router.register(r'people', People, "people")
