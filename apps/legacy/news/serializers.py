from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.accounts.models import Participation, Account
from apps.legacy.account.serializers import ConversionMixin
from apps.teams.models import BaseTeam
from common.fields import HyperlinkedSorlImageField
from apps.legacy.news.models import Membership, Entry

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership


class LegacyMembershipSerializer(ModelSerializer):
    class Meta:
        model = Membership

    user = SlugRelatedField("slug", read_only=True)
    team = SlugRelatedField("slug", read_only=True)


class ConversionMembershipSerializer(ConversionMixin, Serializer):
    conversion_map = {
        "user": None,
        "team": None,
    }

    def create(self, validated_data):
        names = self.keep["user"].split("-")
        if len(names) == 3:
            u = Account.objects.get(first_name=names[0], middle_name=names[1],
                                    last_name=names[2])
        else:
            u = Account.objects.get(first_name=names[0], last_name=names[1])
        e = BaseTeam.objects.get(name=self.keep["team"])
        p = Participation(user=u, group=e.group_set.get(name__endswith="members"),
                          confirmed=True)
        p.save()
        return p


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})

    class Meta:
        model = Entry

