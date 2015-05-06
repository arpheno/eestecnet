from django.test import TestCase

from common.factories import ConfirmableFactory, ConfirmationFactory


__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestConfirmable(TestCase):
    def setUp(self):
        self.object = ConfirmableFactory()

    def test_confirmation_works(self):
        self.assertFalse(self.object.confirmed)
        for c in self.object.confirmation_set.all():
            c.status = True
            c.save()
        self.assertTrue(self.object.confirmed)


class TestConfirmation(TestCase):
    def setUp(self):
        self.object = ConfirmationFactory()


