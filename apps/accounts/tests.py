# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import AnonymousUser
from django.core import mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpRequest
from django.test import TestCase

from apps.accounts.factories import AccountFactory, ParticipationFactory, GroupFactory
from apps.accounts.models import Participation, Account
from apps.accounts.serializers import AccountSerializer, GroupSerializer, \
    ParticipationSerializer
from apps.accounts.views import AccountViewSet, MembershipViewSet
from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from common.tests import RESTCase, ImageCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAccount(RESTCase, TestCase, ImageCase):
    @classmethod
    def setUpClass(cls):
        super(TestAccount, cls).setUpClass()
        cls.object = AccountFactory()

    @classmethod
    def tearDownClass(cls):
        super(TestAccount, cls).tearDownClass()
        cls.object.delete()

    def setUp(self):
        self.object = TestAccount.object
        self.serializer_class = AccountSerializer
        super(TestAccount, self).setUp()
        del self.data['curriculum_vitae']

    def test_password_hashed(self):
        self.assertTrue("$" in Account.objects.get(pk=self.object.pk).password)
    def test_get_short_name(self):
        self.assertEqual(self.object.get_short_name(), u'Łukasz')

    def test_registration_api_register_json(self):
        self.data['email'] = "fake@qq.de"
        response = self.client.post(reverse_lazy('registration_api_register'),
                                    data=json.dumps(self.data),
                                    content_type="application/json")
        self.assertEqual(201, response.status_code)
        a = Account.objects.get(email="fake@qq.de")
        self.assertFalse(a.is_active)
        self.assertTrue("$" in a.password)
        self.assertEqual(len(mail.outbox), 1)
    def test_registration_api_register(self):
        self.data['email'] = "fake@qq.de"
        response = self.client.post(reverse_lazy('registration_api_register'),
                                    data=self.data)
        self.assertEqual(201, response.status_code)
        a = Account.objects.get(email="fake@qq.de")
        self.assertFalse(a.is_active)
        self.assertTrue("$" in a.password)
        self.assertEqual(len(mail.outbox), 1)


    def test_allergies_visible(self):
        r = HttpRequest()
        r.user = AccountFactory()
        r.user.is_superuser = True
        r.method = "GET"
        second = AccountFactory()
        account_detail = AccountViewSet.as_view({'get': 'retrieve'})
        response = account_detail(r, pk=second.pk)
        self.assertEqual(response.status_code, 200)
        response.render()
        self.assertTrue("allergies" in response.content)

    def test_allergies_invisible(self):
        r = HttpRequest()
        r.user = AnonymousUser()
        r.method = "GET"
        second = AccountFactory()
        account_detail = AccountViewSet.as_view({'get': 'retrieve'})
        response = account_detail(r, pk=second.pk)
        response.render()
        print "response:" + response.content
        self.assertTrue("allergies" not in response.content)

    def test_get_commitment(self):
        amsterdam = CommitmentFactory()
        intb = InternationalTeamFactory()
        ParticipationFactory(group=amsterdam.users, user=self.object)
        ParticipationFactory(group=intb.users, user=self.object)
        self.assertEqual(self.object.commitment, amsterdam)


class TestGroup(RESTCase, TestCase):
    def setUp(self):
        self.object = GroupFactory()
        self.serializer_class = GroupSerializer
        super(TestGroup, self).setUp()



class TestParticipation(RESTCase, TestCase):
    def setUp(self):
        self.object = ParticipationFactory()
        self.serializer_class = ParticipationSerializer
        super(TestParticipation, self).setUp()

    def test_participation_has_package(self):
        self.assertTrue(self.object.package.test)

    def test_confirm_participation(self):
        for c in self.object.confirmation_set.all():
            c.confirm()
        self.assertTrue(Participation.objects.get(pk=self.object.pk).confirmed)

    def test_allergies_visible(self):
        r = HttpRequest()
        r.user = AccountFactory()
        self.object.is_superuser = True
        self.object.save()
        r.method = "GET"
        second = ParticipationFactory()
        account_detail = MembershipViewSet.as_view({'get': 'retrieve'})
        response = account_detail(r, pk=second.pk)
        self.assertEqual(response.status_code, 200)
        response.render()
        self.assertTrue("allergies" in response.content)

