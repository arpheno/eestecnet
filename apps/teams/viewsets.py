from rest_framework import viewsets

from apps.events.models import Application
from apps.events.serializers import ApplicationSerializer
from apps.news.models import Membership
from apps.news.serializers import MembershipSerializer
from apps.teams.models import Team
from apps.teams.serializers import CitySerializer
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
    serializer_class = ApplicationSerializer

    def list(self, request, city_pk=None):
        self.queryset = self.queryset.filter(target__pk=city_pk)
        return super(Outgoing, self).list(request)

