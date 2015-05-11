from rest_framework.viewsets import ModelViewSet

from apps.prioritylists.models import PriorityList, Priority
from apps.prioritylists.serializers import PriorityListSerializer, PrioritySerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class PriorityListViewSet(ModelViewSet):
    queryset = PriorityList.objects.all()
    serializer_class = PriorityListSerializer


class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
