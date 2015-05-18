from rest_framework import serializers

from apps.account.serializers import PersonSerializer
from apps.events.models import Event
from apps.teams.serializers import CitySerializer
from eestecnet.fields import HyperlinkedSorlImageField


class EventSerializer(serializers.HyperlinkedModelSerializer):
    members = PersonSerializer(
        many=True,
        read_only=True,
    )
    participants = PersonSerializer(many=True, read_only=True, )
    organizers = PersonSerializer(many=True, read_only=True, )
    organizing_committee = CitySerializer(many=True, read_only=True, )
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})

    class Meta:
        model = Event
        exclude = ['applicants', 'questionaire', 'feedbacksheet', 'pax_report',
                   'organizer_report']

