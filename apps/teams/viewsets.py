from rest_framework import viewsets

from apps.teams.models import Team
from apps.teams.serializers import CitySerializer


class Cities(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.filter(category__in=["lc", "jlc", "observer"])
    serializer_class = CitySerializer

