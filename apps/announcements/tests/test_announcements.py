from django.test import TestCase
from guardian.shortcuts import get_perms

from apps.announcements.factories import AnnouncementFactory, NewsFactory, \
    CareerOfferFactory
from apps.announcements.serializers import AnnouncementSerializer, NewsSerializer, \
    CareerOfferSerializer
from apps.teams.factories import InternationalTeamFactory
from apps.teams.models import BaseTeam
from common.util import RESTCase, AuditCase, ImageCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAnnouncement(RESTCase, AuditCase, TestCase, ImageCase):
    def setUp(self):
        self.ib = InternationalTeamFactory(name="international board")
        self.object = AnnouncementFactory()
        self.serializer_class = AnnouncementSerializer
        super(TestAnnouncement, self).setUp()

    def test_confirmation_created_and_editable_by_international_board(self):
        c = self.object.confirmation_set.all()[0]
        self.assertTrue('change_confirmation' in get_perms(
            BaseTeam.objects.get(name='international board').board, c))


class TestCareerOffer(RESTCase, AuditCase, TestCase):
    def setUp(self):
        self.ib = InternationalTeamFactory(name="international board")
        self.object = CareerOfferFactory()
        self.serializer_class = CareerOfferSerializer
        super(TestCareerOffer, self).setUp()


class TestNews(RESTCase, AuditCase, TestCase):
    def setUp(self):
        self.ib = InternationalTeamFactory(name="international board")
        self.object = NewsFactory()
        self.serializer_class = NewsSerializer
        super(TestNews, self).setUp()

