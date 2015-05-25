from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer

from apps.account.serializers import PersonSerializer, Base64ImageField
from apps.events.models import Event, Participation
from apps.feedback.serializers import LegacyQuestionSetSerializer
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


