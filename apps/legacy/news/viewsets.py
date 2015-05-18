from rest_framework import viewsets

from apps.news.models import Entry, Membership
from apps.news.serializers import EntrySerializer, MembershipSerializer
from eestecnet.serializers import AdminMixin


class Memberships(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class News(AdminMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

