from rest_framework_nested.routers import SimpleRouter

from apps.questionnaires.views import QuestionnaireViewSet, QuestionViewSet, \
    ResponseViewSet, AnswerViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

questionnairerouter = SimpleRouter()
questionnairerouter.register(r'questionnaires', QuestionnaireViewSet)
questionnairerouter.register(r'questions', QuestionViewSet)
questionnairerouter.register(r'responses', ResponseViewSet)
questionnairerouter.register(r'answers', AnswerViewSet)

