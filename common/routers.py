from rest_framework.routers import SimpleRouter

from common.views import ImageViewSet


imagerouter = SimpleRouter()
imagerouter.register(r'images', ImageViewSet)
