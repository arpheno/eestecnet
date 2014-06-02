from datetime import datetime
from django.test import TestCase
from account.models import Eestecer
from events.models import Event
from members.models import Member


class EventTestCase(TestCase):
    def setUp(self):
        Member.objects.create(name="LC Skopje", type='commitment')
        Event.objects.create(name="T4T",
                             summary="Nice event",
                             description="Cool thing",
                             start_date=datetime.now(),
                            # organizing_committee=Member.objects.get(name='LC Skopje'),
                             category="workshop",
                             scope="international",
                             )
        Eestecer.objects.create_superuser("admin@eestec.net", "test")
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        Member.objects.get(name='LC Skopje').members.add(
            Eestecer.objects.get(
                email="admin@eestec.net"
            )
        )
        Member.objects.get(name='LC Skopje').priviledged.add(
            Eestecer.objects.get(
                email="admin@eestec.net"
            )
        )
        self.assertEqual(
         Member.objects.get(name='LC Skopje').member_count(),1
        )
        self.assertEqual(
            Event.objects.get(name='T4T').participant_count(),0
        )