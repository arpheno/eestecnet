from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from apps.accounts.factories import GroupFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestGroup(TestCase, RESTCase):
    def setUp(self):
        self.obj = GroupFactory()
        self.root = "/api"
        self.c = Client()

    def test_get_group_nested(self):
        url = reverse('group-detail',kwargs={'event_pk':self.obj.applicable.pk,'pk':self.obj.pk})
        self.assert_retrieve(url)
        self.assert_retrieve(self.obj.get_absolute_url())

