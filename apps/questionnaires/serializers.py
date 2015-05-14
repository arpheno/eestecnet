from rest_framework.serializers import ModelSerializer

from apps.questionnaires.models import Questionnaire, Question, Response, Answer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question

class QuestionnaireSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('group', 'name', 'question_set')

    question_set = QuestionSerializer(many=True, read_only=True)


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer

class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response
        fields = ('participation', 'name', 'answer_set')

    answer_set = AnswerSerializer(many=True, read_only=True)



