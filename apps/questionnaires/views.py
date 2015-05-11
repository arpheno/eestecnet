from rest_framework.viewsets import ModelViewSet

from apps.questionnaires.models import Question, Questionnaire
from apps.questionnaires.serializers import QuestionnaireSerializer, QuestionSerializer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
class QuestionnaireViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
