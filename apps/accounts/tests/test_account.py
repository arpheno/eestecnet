# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.accounts.factories import AccountFactory, ParticipationFactory, GroupFactory
from apps.accounts.models import Participation, Account
from apps.accounts.serializers import AccountSerializer, GroupSerializer, \
    ParticipationSerializer
from apps.teams.factories import CommitmentFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAccount(RESTCase, TestCase):
    def setUp(self):
        self.object = AccountFactory()
        super(TestAccount, self).setUp()
        self.serializer_class = AccountSerializer

    def test_password_hashed(self):
        self.assertTrue("$" in Account.objects.get(pk=self.object.pk).password)
    def test_get_short_name(self):
        self.assertEqual(self.object.get_short_name(), u'Łukasz')

    def test_get_commitment(self):
        amsterdam = CommitmentFactory()
        ParticipationFactory(group=amsterdam.members, user=self.object)
        self.assertEqual(self.object.commitment, amsterdam)


class TestGroup(RESTCase, TestCase):
    def setUp(self):
        super(TestGroup, self).setUp()
        self.object = GroupFactory()
        self.serializer_class = GroupSerializer

    def test_get_group_nested(self):
        url = reverse('group-detail', kwargs={'event_pk': self.object.applicable.pk,
                                              'pk': self.object.pk})
        self.assert_retrieve(url)


class TestParticipation(RESTCase, TestCase):
    def setUp(self):
        super(TestParticipation, self).setUp()
        self.object = ParticipationFactory()
        self.serializer_class = ParticipationSerializer

    def test_participation_has_package(self):
        self.assertTrue(self.object.package.test)

    def test_confirm_participation(self):
        for c in self.object.confirmation_set.all():
            c.confirm()
        self.assertTrue(Participation.objects.get(pk=self.object.pk).confirmed)



