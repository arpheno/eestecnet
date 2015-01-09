from datetime import timedelta

from django.test import TestCase, Client
from django.utils.timezone import now

from apps.events.models import Application, Event
from apps.teams.tests import EESTECMixin


class EventTestCase(EESTECMixin, TestCase):
    def test_cant_apply_anonymously(self):
        c = Client()
        response = c.get("/events/inktronics/apply")
        self.assertEqual(response.status_code, 403)

    def test_can_get_apply_authenticated(self):
        c = Client()
        c.login(username="user@eestec.net", password="test")
        response = c.get("/events/inktronics/apply")
        self.assertEqual(response.status_code, 200)

    def test_can_post_apply_authenticated(self):
        c = Client()
        c.login(username="user@eestec.net", password="test")
        data = {"letter": "I'm motivated."}
        response = c.post("/events/inktronics/apply", data=data)
        Application.objects.get(applicant=self.user,
                                target=Event.objects.get(slug="inktronics"))

    def test_can_post_edit_application(self):
        c = Client()
        c.login(username="user@eestec.net", password="test")
        data = {"letter": "I'm motivated."}
        response = c.post("/events/inktronics/apply", data=data)
        data = {"letter": "new"}
        response = c.post("/events/inktronics/apply/edit", data=data)
        self.assertEqual(Application.objects.get(applicant=self.user,
                                                 target=Event.objects.get(
                                                     slug="inktronics")).letter, "new")
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


