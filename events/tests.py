from datetime import timedelta
from django.test import TestCase
from django.utils.datetime_safe import datetime
from account.models import Eestecer
from events.admin import MyEventAdmin
from events.models import Event, Application
from members.models import Member


from datetime import date
import warnings

from django import forms
from django.contrib.admin.options import (ModelAdmin, TabularInline,
     HORIZONTAL, VERTICAL)
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.widgets import AdminDateWidget, AdminRadioSelect
from django.contrib.admin.validation import ModelAdminValidator
from django.contrib.admin import (SimpleListFilter,
     BooleanFieldListFilter)
from django.core.exceptions import ImproperlyConfigured
from django.forms.models import BaseModelFormSet
from django.forms.widgets import Select
from django.test import TestCase
from django.utils import six



class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()



class EventTestCase(TestCase):
    def setUp(self):
        self.lc=Member.objects.get(name="Skopje")
        self.ev=Event.objects.create(name="T4T",
                             summary="Nice event",
                             description="Cool thing",
                             start_date=datetime.now(),
                             category="workshop",
                             scope="international",
                             deadline=datetime.now()+timedelta(days=1),
                             )
        self.rec=Event.objects.get(name='skopje recruitment')
        self.admin=Eestecer.objects.create_superuser(
            "admin@eestec.net",
            "test",
            first_name="specific")
        self.user=Eestecer.objects.create_user(
            "user@eestec.net",
            "test",
            first_name="random")
        self.la=Eestecer.objects.create_user(
            "localadmin@eestec.net",
            "test",
            first_name="semi")
        self.site = AdminSite()
        self.ma = MyEventAdmin(self.ev, self.site)

    def test_event_application(self):
        """ assure that accepting applications will add participants"""
        ap=Application.objects.create(
            target=self.ev,
            applicant=self.user,
            letter="lol",
            priority=1)
        self.assertEqual(self.ev.applicants.all()[0],self.user)
        ap.accepted=True
        ap.save()
        self.assertFalse(len(self.ev.applicants.all()))
        self.assertEqual(self.ev.participants.all()[0],self.user)
    def test_lc_application(self):
        """ assure that accepting applications will add participants"""
        ap=Application.objects.create(
            target=self.rec,
            applicant=self.user,
            letter="lol",
            priority=1)
        self.assertEqual(self.rec.applicants.all()[0],self.user)
        ap.accepted=True
        ap.save()
        self.assertFalse(len(self.ev.applicants.all()))
        self.assertEqual(self.lc.members.all()[0],self.user)
    def test_cant_apply_after_deadline(self):
        ap=Application.objects.create(
            target=self.rec,
            applicant=self.user,
            letter="lol",
            priority=1)
        ap.date=ap.date+timedelta(days=2)
        ap.save()
        self.assertFalse(len(self.ev.applicants.all()))
    def test_cant_apply_twice(self):
        ap=Application.objects.create(
            target=self.rec,
            applicant=self.user,
            letter="lol",
            priority=1)
        ap.save()
        err=0
        try:
            ap=Application.objects.create(
                target=self.rec,
                applicant=self.user,
                letter="lola",
                priority=1)
            ap.save()
        except:
            err=1

        self.assertEqual(err,1)


