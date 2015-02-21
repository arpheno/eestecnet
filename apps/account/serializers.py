from django.contrib.auth.models import Group
from rest_framework import serializers

from apps.account.models import Eestecer
from eestecnet.fields import HyperlinkedSorlImageField


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group


class PersonParticipationSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="500x500",
                                          options={'crop': 'center'})

    class Meta:
        model = Eestecer
        exclude = ('email', 'password')
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})
    class Meta:
        model = Eestecer
        fields = (
        'thumbnail', 'first_name', 'middle_name', 'last_name', 'second_last_name',
        'is_superuser', 'slug', 'field_of_study', 'groups', 'user_permissions')
        # exclude=('email','password','passport_number','date_of_birth')
