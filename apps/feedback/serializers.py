from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer
from apps.events.models import Participation
from apps.feedback.models import Question, QuestionSet


class LegacyQuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        exclude =  ['parent']
class LegacyQuestionSetSerializer(ModelSerializer):
    class Meta:
        model = QuestionSet
        exclude =  ['parents']
    question_set = LegacyQuestionSerializer(many=True,read_only=True)
class LegacyParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation
    participant = SlugRelatedField("slug", read_only=True)
    target = SlugRelatedField("slug", read_only=True)
