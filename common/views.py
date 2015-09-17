from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from common.models import Image, Content
from common.serializers import ImageSerializer, ContentOutSerializer, ContentInSerializer

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentOutSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method in ["PUT", "POST"]:
            return ContentInSerializer
        return ContentOutSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
