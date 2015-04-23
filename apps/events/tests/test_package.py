from unittest import TestCase

from apps.events.factories import PackageFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestPackage(TestCase):
    def setUp(self):
        self.object = PackageFactory()
