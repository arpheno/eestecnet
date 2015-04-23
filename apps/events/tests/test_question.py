from django.test import TestCase

from apps.events.factories import QuestionFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestQuestion(TestCase):
    def test_create(self):
        QuestionFactory()
