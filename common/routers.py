from rest_framework.routers import SimpleRouter

from common.views import ImageViewSet, ContentViewSet

imagerouter = SimpleRouter()
imagerouter.register(r'images', ImageViewSet)
contentrouter = SimpleRouter()
contentrouter.register(r'content', ContentViewSet)
