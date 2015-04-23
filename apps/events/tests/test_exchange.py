from unittest import TestCase

from apps.events.factories import ExchangeFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestExchange(TestCase):
    def setUp(self):
        self.object = ExchangeFactory()
