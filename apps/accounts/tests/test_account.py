# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.accounts.factories import AccountFactory, ParticipationFactory, GroupFactory
from apps.teams.factories import CommitmentFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAccount(RESTCase,TestCase):
    def setUp(self):
        self.object = AccountFactory()
        super(TestAccount,self).setUp()

    def test_get_short_name(self):
        self.assertEqual(self.object.get_short_name(), 'Łukasz')
    def test_get_commitment(self):
        amsterdam = CommitmentFactory()
        ParticipationFactory(group=amsterdam.members, user=self.object)
        self.assertEqual(self.object.commitment, amsterdam)

    def test_assert_retrieve(self):
        self.assert_retrieve(self.object.get_absolute_url())


class TestGroup(RESTCase, TestCase):
    def setUp(self):
        super(TestGroup, self).setUp()
        self.object = GroupFactory()

    def test_get_group_nested(self):
        url = reverse('group-detail', kwargs={'event_pk': self.object.applicable.pk,
                                              'pk': self.object.pk})
        self.assert_retrieve(url)


class TestParticipation(RESTCase, TestCase):
    def setUp(self):
        super(TestParticipation, self).setUp()
        self.object = ParticipationFactory()

    def test_participation_has_package(self):
        self.assertTrue(self.object.package.test)
