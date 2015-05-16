from django.test import TestCase

from common.factories import ConfirmableFactory, ConfirmationFactory, ImageFactory, \
    ReportFactory
from common.serializers import ImageSerializer
from common.util import RESTCase


__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestConfirmable(TestCase):
    def setUp(self):
        self.object = ConfirmableFactory()

    def test_confirmation_works(self):
        self.assertFalse(self.object.confirmed)
        for c in self.object.confirmation_set.all():
            c.status = True
            c.save()
        self.assertTrue(self.object.confirmed)


class TestConfirmation(TestCase):
    def setUp(self):
        self.object = ConfirmationFactory()


class TestReport(TestCase):
    def test_can_construct(self):
        self.object = ReportFactory()
class TestImage(RESTCase, TestCase):
    def setUp(self):
        self.object = ImageFactory()
        self.serializer_class = ImageSerializer
        super(TestImage, self).setUp()
        import base64

        with self.object.full_size as image_file:
            imagedata = base64.b64encode(image_file.read())
        self.data['full_size'] = imagedata
