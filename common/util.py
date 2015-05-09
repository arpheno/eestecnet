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


    def assert_create(self, url, data):
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 201)
    def assert_retrieve(self, url):
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def assert_update(self, url, data):
        response = self.c.get(url)
        self.assertIn(response.status_code, [200, 202, 204])

    def assert_delete(self, url):
        response = self.c.delete(url)
        self.assertIn(response.status_code, [200, 202, 204])

    def test_rest_list_resource(self):
        self.assert_retrieve(
            reverse_lazy(self.object._meta.object_name.lower() + '-list'))

    def test_rest_retrieve_resource(self):
        url = self.object.get_absolute_url()
        self.assert_retrieve(url)

    def test_rest_create_resource(self):
        data = self.serializer_class(self.object)
        url = reverse_lazy(self.object._meta.object_name.lower() + '-list')
        self.assert_create(url, data)

    def test_rest_update_resource(self):
        data = self.serializer_class(self.object)
        url = reverse_lazy(self.object._meta.object_name.lower() + '-list')
        self.assert_create(url, data)
        url = reverse_lazy(self.object._meta.object_name.lower() + '-detail')
        self.assert_update(url, data)

    def test_rest_delete_resource(self):
        data = self.serializer_class(self.object)
        url = reverse_lazy(self.object._meta.object_name.lower() + '-list')
        self.assert_create(url, data)
        url = reverse_lazy(self.object._meta.object_name.lower() + '-detail')
        self.assert_delete(url)
