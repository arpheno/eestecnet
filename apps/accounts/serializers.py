from rest_framework.fields import CharField
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Group, Account, Participation
from common.serializers import ImageSerializer, ImageMixin

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

ACCOUNT_PUBLIC = ['name', 'id', 'first_name', 'middle_name', 'last_name', 'second_last_name', 'images']
ACCOUNT_EVENT = ['name', 'tshirt_size', 'allergies', 'food_preferences', 'passport_number',
                 'mobile']


class AccountSerializer(ImageMixin, ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login']

    images = ImageSerializer(many=True)
    name = CharField(read_only=True)


class UnprivilegedAccountSerializer(AccountSerializer):
    class Meta:
        model = Account
        fields = ACCOUNT_PUBLIC

    images = ImageSerializer(many=True, read_only=True)


class ParticipationAccountSerializer(AccountSerializer):
    class Meta:
        model = Account
        fields = ACCOUNT_PUBLIC + ACCOUNT_EVENT

    images = ImageSerializer(many=True, read_only=True)


class ParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation


class ReadParticipationSerializer(ParticipationSerializer):
    class Meta:
        model = Participation

    user = ParticipationAccountSerializer(read_only=True)


class GroupSerializer(ModelSerializer):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    user_set = UnprivilegedAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Group
