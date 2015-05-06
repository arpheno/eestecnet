from django.test import TestCase

from apps.accounts.factories import ParticipationFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestParticipation(RESTCase,TestCase):
    def setUp(self):
        super(TestParticipation,self).setUp()
        self.object = ParticipationFactory()

    def test_participation_has_package(self):
        self.assertTrue(self.object.package.test)
    def test_api(self):
        self.assert_retrieve(self.object.get_absolute_url())

