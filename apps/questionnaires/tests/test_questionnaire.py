from django.test import TestCase

from apps.questionnaires.factories import QuestionnaireFactory


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestQuestionnaire(TestCase):
    def test_create(self):
        QuestionnaireFactory()
