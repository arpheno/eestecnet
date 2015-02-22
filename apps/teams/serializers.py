from rest_framework import serializers

from apps.account.serializers import PersonSerializer
from apps.news.serializers import MembershipSerializer
from apps.teams.models import Team
from eestecnet.fields import HyperlinkedSorlImageField


class CityListSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        dimensions="200x200",
        options={'crop': 'center'}
    )

    class Meta:
        model = Team
        fields = ('thumbnail', 'name')


class CityDetailSerializer(serializers.HyperlinkedModelSerializer):
    users = PersonSerializer(
        many=True,
        read_only=True,
    )
    thumbnail = HyperlinkedSorlImageField(
        dimensions="200x200",
        options={'crop': 'center'}
    )
    membership_set = MembershipSerializer(many=True, read_only=True)
    class Meta:
        model = Team

