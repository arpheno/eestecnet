import logging

from django.contrib.auth.models import Permission
from rest_framework import serializers, viewsets


logger = logging.getLogger(__name__)


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission


class Permissions(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class AdminMixin(object):
    def get_serializer(self, *args, **kwargs):
        serializer = super(AdminMixin, self).get_serializer(*args, **kwargs)
        return serializer

