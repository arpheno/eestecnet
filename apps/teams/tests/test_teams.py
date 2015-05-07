from django.test import TestCase

from apps.accounts.factories import ParticipationFactory

from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestTeam(object):
    def test_applications_work(self):
        p = ParticipationFactory(group=self.object.officials)
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
class TestCommitment(RESTCase, TestCase):
    def setUp(self):
        super(TestCommitment, self).setUp()
        self.object = CommitmentFactory()


class TestInternationalTeam(RESTCase, TestCase):
    def setUp(self):
        super(TestCommitment, self).setUp()
        self.object = InternationalTeamFactory()

