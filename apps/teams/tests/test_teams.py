from django.test import TestCase

from apps.accounts.factories import ParticipationFactory
from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from apps.teams.serializers import CommitmentSerializer, InternationalTeamSerializer
from common.util import RESTCase, AuditCase, ImageCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestTeam(TestCase, AuditCase, ImageCase):
    def setUp(self):
        super(TestTeam, self).setUp()
        self.object = CommitmentFactory()
        self.serializer_class = CommitmentSerializer
    def test_applications_work(self):
        p = ParticipationFactory(group=self.object.members)
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
        self.serializer_class = CommitmentSerializer
        super(TestCommitment, self).setUp()


class TestInternationalTeam(RESTCase, AuditCase, TestCase):
    def setUp(self):
        self.object = InternationalTeamFactory()
        self.serializer_class = InternationalTeamSerializer
        super(TestInternationalTeam, self).setUp()

