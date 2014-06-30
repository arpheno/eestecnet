from django.contrib.auth.models import Group
from django.test import TestCase
from django.utils.datetime_safe import datetime
from account.models import Eestecer
from events.models import Event, Application
from members.models import Member


class MemberTestCase(TestCase):
    def setUp(self):
        self.lc=Member.objects.create(name="Skopje", type='commitment')
        self.ev=Event.objects.create(name="T4T",
                                     summary="Nice event",
                                     description="Cool thing",
                                     start_date=datetime.now(),
                                     category="workshop",
                                     scope="international",
                                     )
        self.user=Eestecer.objects.create_superuser("admin@eestec.net", "test")
        self.lc.members.add(self.user)

    def test_gain_privileges(self):
        """ assure that accepting applications will add participants"""
        self.assertFalse(len(self.lc.priviledged.all()))
        self.lc.priviledged.add(self.user)
        self.assertTrue(len(self.lc.priviledged.all()))
