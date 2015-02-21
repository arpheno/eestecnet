from rest_framework import serializers

from apps.news.models import Entry, Membership
from eestecnet.fields import HyperlinkedSorlImageField


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})

    class Meta:
        model = Entry

