from rest_framework.serializers import ModelSerializer

from apps.questionnaires.models import Questionnaire, Question, Response, Answer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionnaireSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question


class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer