from django.test import TestCase, Client
from rest_framework.reverse import reverse_lazy

from apps.events.factories import BaseEventFactory, ParticipationFactory
from common.util import RESTCase


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestBaseEvent(TestCase, RESTCase):
    def setUp(self):
        self.object = BaseEventFactory()
        self.c = Client()

    def test_organizers_can_modify_event(self):
        p = ParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_baseevent', self.object))

    def test_list_events(self):
        self.assert_retrieve(reverse_lazy('baseevent-list'))
