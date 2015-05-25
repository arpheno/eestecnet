from rest_framework.relations import StringRelatedField, SlugRelatedField
from rest_framework.serializers import ModelSerializer
from apps.account.models import Eestecer
from apps.account.serializers import Base64ImageField, Base64PdfField
from apps.events.models import Event, Participation, EventImage
from apps.feedback.serializers import LegacyQuestionSetSerializer
from apps.teams.models import Team, MemberImage


class LegacyAccountSerializer(ModelSerializer):
    class Meta:
        model = Eestecer
    thumbnail = Base64ImageField(
        max_length=None, use_url=True,
    )
    curriculum_vitae= Base64PdfField(
        max_length=None, use_url=True,
    )

class LegacyTeamImageSerializer(ModelSerializer):
    class Meta:
        model = MemberImage
    property = StringRelatedField(read_only=True)
    image = Base64ImageField(max_length=0,use_url=True)
class LegacyTeamSerializer(ModelSerializer):
    class Meta:
        model = Team
    thumbnail = Base64ImageField(
        max_length=None, use_url=True,required=False
    )
    users = StringRelatedField(many=True,read_only=True)
    images= LegacyTeamImageSerializer(many=True,read_only=True)
class LegacyEventImageSerializer(ModelSerializer):
    class Meta:
        model = EventImage
    property = StringRelatedField(read_only=True)
    image = Base64ImageField(max_length=0,use_url=True)
class LegacyEventSerializer(ModelSerializer):
    class Meta:
        model = Event
    questionaire = LegacyQuestionSetSerializer(read_only=True)
    feedbacksheet = LegacyQuestionSetSerializer(read_only=True)
    organizers = StringRelatedField(many=True, read_only=True)
    members = StringRelatedField(many=True, read_only=True)
    organizing_committee = SlugRelatedField("slug",many=True, read_only=True)
    thumbnail = Base64ImageField(max_length=0,use_url=True)
    images= LegacyEventImageSerializer(many=True,read_only=True)
class LegacyParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation
    participant = StringRelatedField(read_only=True)
    target = StringRelatedField( read_only=True)

