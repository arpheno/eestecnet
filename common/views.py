from rest_framework.viewsets import ModelViewSet

from common.models import Image
from common.serializers import ImageSerializer


__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
