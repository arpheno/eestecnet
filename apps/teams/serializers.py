from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from apps.account.serializers import PersonSerializer, Base64ImageField
from apps.teams.models import Team
from eestecnet.fields import HyperlinkedSorlImageField


class CitySerializer(serializers.HyperlinkedModelSerializer):
    members = PersonSerializer(
        many=True,
        read_only=True,
    )
    thumbnail = HyperlinkedSorlImageField(
        dimensions="200x200",
        options={'crop': 'center'}
    )

    class Meta:
        model = Team
class LegacyTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
    thumbnail = Base64ImageField(
        max_length=None, use_url=True,required=False
    )
    members = StringRelatedField(many=True,read_only=True)
