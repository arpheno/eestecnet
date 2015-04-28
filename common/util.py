from django.test import Client

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RESTCase(object):
    def setUp(self):
        self.c = Client()
        super(RESTCase, self).setUp()

    def assert_retrieve(self, url):
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

