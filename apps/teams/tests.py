from django.test import TestCase

from apps.accounts.factories import ParticipationFactory
from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from apps.teams.models import Commitment
from apps.teams.serializers import team_serializer_factory
from common.tests import RESTCase, ImageCase, AuditCase

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestTeam(TestCase, AuditCase, ImageCase):
    def setUp(self):
        super(TestTeam, self).setUp()
        self.object = CommitmentFactory()
        self.serializer_class = team_serializer_factory(Commitment)

    def test_applications_work(self):
        p = ParticipationFactory(group=self.object.users)
        self.assertTrue(p.user in self.object.applicants)
        self.assertTrue(p in self.object.applications)
        self.assertFalse(p.user in self.object.participants)
        self.assertFalse(p in self.object.participations)
        for c in p.confirmation_set.all():
            c.confirm()
        self.assertFalse(p.user in self.object.applicants)
        self.assertFalse(p in self.object.applications)
        self.assertTrue(p.user in self.object.participants)
        self.assertTrue(p in self.object.participations)


class TestCommitment(RESTCase, AuditCase, TestCase):
    def setUp(self):
        self.object = CommitmentFactory()
        self.serializer_class = team_serializer_factory(Commitment)
        super(TestCommitment, self).setUp()


class TestInternationalTeam(RESTCase, AuditCase, TestCase):
    def setUp(self):
        self.object = InternationalTeamFactory()
        self.serializer_class = team_serializer_factory(Commitment)
        super(TestInternationalTeam, self).setUp()
