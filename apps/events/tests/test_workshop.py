from unittest import TestCase

from apps.events.factories import WorkshopFactory, WorkshopParticipationFactory


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestWorkshop(TestCase):
    def setUp(self):
        self.object = WorkshopFactory()

    def test_organizers_can_modify_event(self):
        p = WorkshopParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_workshop', self.object))
