from rest_framework.relations import SlugRelatedField

from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Participation

from apps.legacy.feedback.models import Question, QuestionSet


class LegacyQuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        exclude = ['parent']


class LegacyQuestionSetSerializer(ModelSerializer):
    class Meta:
        model = QuestionSet
        exclude = ['parents']

    question_set = LegacyQuestionSerializer(many=True, read_only=True)


class LegacyParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation

    participant = SlugRelatedField("slug", read_only=True)
    target = SlugRelatedField("slug", read_only=True)
