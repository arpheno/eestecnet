from django.test import TestCase

from apps.prioritylists.factories import PriorityListFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestPriorityList(RESTCase, TestCase):
    def setUp(self):
        self.object = PriorityListFactory()

