from rest_framework import serializers

from apps.account.serializers import PersonSerializer
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
        fields = ('name', 'thumbnail', 'members')

