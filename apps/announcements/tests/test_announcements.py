from django.test import TestCase
from guardian.shortcuts import get_perms

from apps.announcements.factories import AnnouncementFactory
from apps.announcements.serializers import AnnouncementSerializer
from apps.teams.factories import InternationalTeamFactory
from apps.teams.models import BaseTeam
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAnnouncement(RESTCase, TestCase):
    def setUp(self):
        super(TestAnnouncement, self).setUp()
        self.ib = InternationalTeamFactory(name="international board")
        self.object = AnnouncementFactory()
        self.serializer_class = AnnouncementSerializer

    def test_confirmation_created_and_editable_by_international_board(self):
        c = self.object.confirmation_set.all()[0]
        self.assertTrue('change_confirmation' in get_perms(
            BaseTeam.objects.get(name='international board').board, c))
