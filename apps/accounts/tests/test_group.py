from unittest import TestCase

from django.test import Client

from apps.events.factories import GroupFactory
from common.util import RESTCase


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestGroup(TestCase, RESTCase):
    def setUp(self):
        self.obj = GroupFactory()
        self.root = "/api"
        self.c = Client()

    def test_get_group_nested(self):
        url = self.root + "/events/" + self.obj.applicable.pk + "/packages/"
        self.assert_retrieve(url)
        url = self.root + "/events/" + self.obj.applicable.pk + "/packages/" + \
              self.obj.pk + "/"
        self.assert_retrieve(url)

