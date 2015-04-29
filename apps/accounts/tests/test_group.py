from unittest import TestCase

from apps.events.factories import GroupFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestGroup(TestCase):
    def setUp(self):
        self.obj = GroupFactory()

