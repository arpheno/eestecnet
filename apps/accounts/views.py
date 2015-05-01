from rest_framework.viewsets import ModelViewSet
from apps.accounts.models import Group, Account, Participation
from apps.accounts.serializers import GroupSerializer, AccountSerializer, \
    ParticipationSerializer

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def list(self, request, group_pk=None):
        self.queryset = self.queryset.filter(groups=group_pk)
        return super(AccountViewSet, self).list(request)

    def retrieve(self, request, pk=None, group_pk=None):
        self.object = self.queryset.get(pk=pk, groups=group_pk)
        return super(AccountViewSet, self).retrieve(request)

class MembershipViewSet(ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    def list(self, request, group_pk=None):
        self.queryset = self.queryset.filter(groups=group_pk)
        return super(MembershipViewSet, self).list(request)

    def retrieve(self, request, pk=None, group_pk=None):
        self.object = self.queryset.get(pk=pk, group=group_pk)
        return super(MembershipViewSet, self).retrieve(request)
