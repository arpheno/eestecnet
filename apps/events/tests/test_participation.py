from unittest import TestCase

from apps.events.factories import ParticipationFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestParticipation(TestCase):
    def setUp(self):
        self.object = ParticipationFactory()

    def test_participation_has_package(self):
        print self.object.package.test
