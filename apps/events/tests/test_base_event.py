from django.test import TestCase

from apps.events.factories import BaseEventFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestBaseEvent(TestCase):
    def test_create(self):
        BaseEventFactory()
