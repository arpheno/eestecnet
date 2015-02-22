from rest_framework import viewsets
from rest_framework.filters import DjangoObjectPermissionsFilter

from apps.events.models import Application
from apps.events.serializers import OutgoingSerializer
from apps.news.models import Membership
from apps.news.serializers import MembershipSerializer
from apps.teams.models import Team
from apps.teams.serializers import CitySerializer
from eestecnet import permissions
from eestecnet.serializers import AdminMixin


class TeamMembers(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def list(self, request, city_pk=None):
        self.queryset = self.queryset.filter(team__pk=city_pk)
        return super(TeamMembers, self).list(request)
class Cities(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = CitySerializer


class Outgoing(viewsets.ReadOnlyModelViewSet):
    queryset = Application.objects.all()
    serializer_class = OutgoingSerializer
    filter_backends = [DjangoObjectPermissionsFilter]
    permission_classes = [permissions.CustomObjectPermissions]

    def list(self, request, city_pk=None):
        self.queryset = self.queryset.filter(applicant__teams=city_pk)
        return super(Outgoing, self).list(request)

