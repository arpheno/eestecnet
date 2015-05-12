from rest_framework.viewsets import ModelViewSet

from apps.questionnaires.models import Question, Questionnaire, Response, Answer
from apps.questionnaires.serializers import QuestionnaireSerializer, \
    QuestionSerializer, \
    ResponseSerializer, AnswerSerializer


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


class ResponseViewSet(ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
