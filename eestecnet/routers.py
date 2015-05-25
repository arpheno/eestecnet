from rest_framework import routers

from apps.account.viewsets import People, GroupViewset
from apps.news.viewsets import News, Memberships
from eestecnet.serializers import Permissions


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'people', People)
router.register(r'news', News)
router.register(r'memberships', Memberships)
router.register(r'groups', GroupViewset)
router.register(r'permissions', Permissions)

