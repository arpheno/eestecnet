from django.test import TestCase

from apps.questionnaires.factories import QuestionnaireFactory, QuestionFactory
from apps.questionnaires.serializers import QuestionnaireSerializer, QuestionSerializer
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestQuestionnaire(RESTCase, TestCase):
    def setUp(self):
        super(TestQuestionnaire, self).setUp()
        self.object = QuestionnaireFactory()
        self.serializer_class = QuestionnaireSerializer


class TestQuestion(RESTCase, TestCase):
    def setUp(self):
        super(TestQuestion, self).setUp()
        self.object = QuestionFactory()
        self.serializer_class = QuestionSerializer

