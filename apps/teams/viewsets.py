from rest_framework import viewsets
from rest_framework.filters import DjangoObjectPermissionsFilter
from apps.news.models import Membership
from apps.news.serializers import MembershipSerializer

from eestecnet import permissions
from eestecnet.serializers import AdminMixin


class TeamMembers(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def list(self, request, city_pk=None):
        self.queryset = self.queryset.filter(team__pk=city_pk)
        return super(TeamMembers, self).list(request)



