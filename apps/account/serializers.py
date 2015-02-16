from rest_framework import serializers

from apps.account.models import Eestecer


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eestecer
        fields = ('name', 'thumbnail')
