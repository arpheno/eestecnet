from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.accounts.models import Account, Participation
from apps.accounts.serializers import AccountSerializer, \
    ParticipationSerializer, UnprivilegedAccountSerializer, ReadParticipationSerializer

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_superuser or self.request.method.lower() == "post" or \
                                self.action == 'retrieve' and self.get_object() == \
                        self.request.user:
            return AccountSerializer
        else:
            return UnprivilegedAccountSerializer

    def list(self, request):
        self.queryset = self.queryset
        return super(AccountViewSet, self).list(request)

    def retrieve(self, request, pk=None, group_pk=None):
        self.object = self.queryset.get(pk=pk, groups=group_pk)
        return super(AccountViewSet, self).retrieve(request)

class MembershipViewSet(ModelViewSet):
    queryset = Participation.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReadParticipationSerializer
        return ParticipationSerializer
    def list(self, request, group_pk=None):
        if group_pk:
            self.queryset = self.queryset.filter(groups=group_pk)
        else:
            pass
        return super(MembershipViewSet, self).list(request)

    def retrieve(self, request, pk=None, group_pk=None):
        self.object = self.queryset.get(pk=pk)
        return super(MembershipViewSet, self).retrieve(request)
