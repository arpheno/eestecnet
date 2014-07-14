from django.core.exceptions import ValidationError

from django.core.files import File
from django.test import TestCase
from django.utils.datetime_safe import datetime

from account.models import Eestecer

from events.models import Event
from members.models import Member


class MemberTestCase(TestCase):
    def setUp(self):
        self.lc = Member.objects.get(name='skopje')
        self.ev = Event.objects.create(name="T4T",
                                       summary="Nice event",
                                       description="Cool thing",
                                       start_date=datetime.now(),
                                       category="workshop",
                                       scope="international",
        )
        self.user = Eestecer.objects.create_superuser("admin@eestec.net", "test")
        self.lc.members.add(self.user)

    def test_gain_privileges(self):
        """ assure that accepting applications will add participants"""
        self.assertFalse(len(self.lc.priviledged.all()))
        self.lc.priviledged.add(self.user)
        self.assertTrue(len(self.lc.priviledged.all()))

    def test_credit_for_image_required(self):
        with open('eestecnet\\lc\\test.png', 'rb') as doc_file:
            self.lc.thumbnail.save('test.png', File(doc_file), save=True)
        try:
            self.lc.clean()
            raise AssertionError()
        except ValidationError:
            pass