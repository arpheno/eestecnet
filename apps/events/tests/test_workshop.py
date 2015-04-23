from unittest import TestCase

from apps.events.factories import WorkshopFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestWorkshop(TestCase):
    def setUp(self):
        self.object = WorkshopFactory()
