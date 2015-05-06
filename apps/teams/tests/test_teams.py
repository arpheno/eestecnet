from django.test import TestCase

from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestCommitment(RESTCase, TestCase):
    def setUp(self):
        self.object = CommitmentFactory()


class TestInternationalTeam(RESTCase, TestCase):
    def setUp(self):
        self.object = InternationalTeamFactory()

