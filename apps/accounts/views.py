from rest_framework.decorators import list_route
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
        print self.request.user.is_superuser
        if self.request.user.is_superuser or \
                        self.request.method.lower() == "post" or \
                                self.action in ['put', 'retrieve'] and self.get_object() == \
                        self.request.user:
            return AccountSerializer
        else:
            return UnprivilegedAccountSerializer

    @list_route()
    def me(self, request):
        self.kwargs["pk"] = self.request.user.id
        return super(AccountViewSet, self).retrieve(request, pk=self.request.user.id)


class MembershipViewSet(ModelViewSet):
    queryset = Participation.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReadParticipationSerializer
        return ParticipationSerializer
