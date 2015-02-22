from rest_framework import serializers

from apps.account.serializers import PersonSerializer, PersonParticipationSerializer
from apps.events.models import Event, Participation, Transportation, Application
from apps.feedback.serializers import AnswerSetSerializer
from apps.teams.serializers import CitySerializer
from eestecnet.fields import HyperlinkedSorlImageField


class TransportationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transportation


class IncomingSerializer(serializers.ModelSerializer):
    applicant = PersonSerializer(read_only=True)
    questionaire = AnswerSetSerializer(read_only=True)
    class Meta:
        model = Application


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = PersonSerializer(read_only=True)
    questionaire = AnswerSetSerializer()

    class Meta:
        model = Application


class OutgoingSerializer(serializers.ModelSerializer):
    applicant = PersonSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ('applicant', 'target', 'priority')

class ParticipationSerializer(serializers.HyperlinkedModelSerializer):
    participant = PersonParticipationSerializer(read_only=True, )
    feedback = AnswerSetSerializer(read_only=True)
    transportation = TransportationSerializer(read_only=True)

    class Meta:
        model = Participation
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

