from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from events.models import Application
from teams.tests import EESTECMixin


class EventTestCase(EESTECMixin, TestCase):

    def test_event_application(self):
        """ assure that accepting applications will add participants"""
        ap = Application.objects.create(
            target=self.inktronics,
            applicant=self.user,
            letter="lol",
            priority=1)
        self.assertEqual(self.inktronics.applicants.all()[0], self.user)
        ap.accepted = True
        ap.save()
        self.assertEqual(self.inktronics.participants.all()[0], self.user)

    def test_cant_apply_after_deadline(self):
        for application in Application.objects.all():
            application.delete()
        self.assertFalse(len(self.inktronics.applicants.all()))

        ap = Application.objects.create(
            target=self.inktronics,
            applicant=self.user,
            letter="lol",
            priority=1,
            date=now() + timedelta(days=15)
        )
        ap.save()
        self.assertFalse(len(self.inktronics.applicants.all()))

    def test_cant_apply_twice(self):
        ap = Application.objects.create(
            target=self.inktronics,
            applicant=self.user,
            letter="lol",
            priority=1)
        ap.save()
        err = 0
        ap.letter = "lola"
        ap.save()
        number_of_applications = len(Application.objects.filter(
            target=self.inktronics,
            applicant=self.user))
        self.assertEqual(number_of_applications, 1)


