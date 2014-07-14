from django.core.exceptions import ValidationError

from django.core.files import File
from django.db.models import get_model
from django.test import TestCase
from django.utils.datetime_safe import datetime


Eestecer = get_model('account', 'Eestecer')
from events.models import Event
from teams.models import Team


class MemberTestCase(TestCase):
    def setUp(self):
        self.lc = Team.objects.get(name='skopje')
        self.ev = Event.objects.create(name="T4T",
                                       summary="Nice event",
                                       description="Cool thing",
                                       start_date=datetime.now(),
                                       category="workshop",
                                       scope="international",
        )
        self.user = Eestecer.objects.create_superuser("admin@eestec.net", "test")
        self.lc.users.add(self.user)

    def test_gain_privileges(self):
        """ assure that accepting applications will add participants"""
        self.assertFalse(len(self.lc.privileged.all()))
        self.lc.privileged.add(self.user)
        self.assertTrue(len(self.lc.privileged.all()))

    def test_credit_for_image_required(self):
        with open('eestecnet\\lc\\test.png', 'rb') as doc_file:
            self.lc.thumbnail.save('test.png', File(doc_file), save=True)
        try:
            self.lc.clean()
            raise AssertionError()
        except ValidationError:
            pass