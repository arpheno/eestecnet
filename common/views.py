from rest_framework.viewsets import ModelViewSet

from common.models import Image, Content
from common.serializers import ImageSerializer, ContentSerializer

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
