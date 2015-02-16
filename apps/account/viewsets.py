from rest_framework import viewsets

from apps.account.models import Eestecer
from apps.account.serializers import PersonSerializer


class People(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Eestecer.objects.all()
        else:
            return self.request.user

    model = Eestecer
    serializer_class = PersonSerializer

