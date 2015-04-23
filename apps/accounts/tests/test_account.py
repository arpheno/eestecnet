# -*- coding: utf-8 -*-
from unittest import TestCase

from apps.accounts.factories import AccountFactory


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestAccount(TestCase):
    def setUp(self):
        self.user = AccountFactory()

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Łukasz')