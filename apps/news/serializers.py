from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer

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

class LegacyMembershipSerializer(ModelSerializer):
    class Meta:
        model = Membership

    user = StringRelatedField( read_only=True)
    team = StringRelatedField(read_only=True)

