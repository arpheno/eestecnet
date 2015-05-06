from django.test import TestCase

from apps.questionnaires.factories import QuestionnaireFactory, QuestionFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestQuestionnaire(RESTCase, TestCase):
    def setUp(self):
        self.object = QuestionnaireFactory()


class TestQuestion(RESTCase, TestCase):
    def setUp(self):
        self.object = QuestionFactory()

