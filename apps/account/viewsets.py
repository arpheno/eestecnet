from django.contrib.auth.models import Group
from rest_framework import viewsets

from apps.account.models import Eestecer
from apps.account.serializers import PersonSerializer, GroupSerializer
from eestecnet.serializers import AdminMixin


class GroupViewset(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class People(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Eestecer.objects.all()
    serializer_class = PersonSerializer

