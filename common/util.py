from django.core.urlresolvers import reverse_lazy
from django.test import Client

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RESTCase(object):
    """
    Mixin that combines common functionality for testing the REST API.
    By default will also test the list and absolute endpoints of a resource.
    To use this mixin the child testcase must create a self.object resource.
    """
    def setUp(self):
        self.c = Client()
        self.root = "/api"
        super(RESTCase, self).setUp()


    def assert_retrieve(self, url):
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_rest_list_resource(self):
        self.assert_retrieve(
            reverse_lazy(self.object._meta.object_name.lower() + '-list'))

    def test_rest_detail_resource(self):
        self.assert_retrieve(self.object.get_absolute_url())
