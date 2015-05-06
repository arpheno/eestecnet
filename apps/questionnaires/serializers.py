from rest_framework.serializers import ModelSerializer

from apps.questionnaires.models import Questionnaire


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionnaireSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire
