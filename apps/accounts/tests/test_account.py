# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.accounts.factories import AccountFactory
from common.util import RESTCase


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAccount(RESTCase,TestCase):
    def setUp(self):
        self.user = AccountFactory()
        super(TestAccount,self).setUp()

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Łukasz')

    def test_assert_retrieve(self):
        self.assert_retrieve(self.user.get_absolute_url())
