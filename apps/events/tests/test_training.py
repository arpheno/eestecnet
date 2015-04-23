from unittest import TestCase

from apps.events.factories import TrainingFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestTraining(TestCase):
    def setUp(self):
        self.object = TrainingFactory()
