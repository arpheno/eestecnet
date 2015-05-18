from rest_framework import viewsets

from apps.legacy.account.models import Eestecer
from apps.legacy.account.serializers import PersonSerializer


class People(viewsets.ModelViewSet):
    queryset = Eestecer.objects.all()
    serializer_class = PersonSerializer

