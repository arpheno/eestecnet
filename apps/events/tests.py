import json
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client
from guardian.shortcuts import get_perms
import pytest
from rest_framework.renderers import JSONRenderer

from apps.accounts.factories import ParticipationFactory, AccountFactory
from apps.accounts.models import Account
from apps.events.models import Exchange, Training, Workshop
from apps.events.serializers import Detail, detail_factory, TravelSerializer
from apps.events.factories import BaseEventFactory, ParticipationConfirmationFactory, \
    ExchangeFactory, TrainingFactory, WorkshopFactory, WorkshopParticipationFactory, \
    TravelFactory
from common.factories import ReportFactory
from common.models import Confirmable, Confirmation
from common.tests import RESTCase, ImageCase, AuditCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def eestecer():
    hans=AccountFactory(first_name="Hans",is_active=True,is_superuser=False)
    hans.set_password("default")
    hans.save()
    myadmin = Client()
    myadmin.login(username=hans.email, password="default")
    return myadmin

def admin():
    peter = AccountFactory(first_name="Peter",is_active=True,is_superuser=True)
    peter.set_password("default")
    peter.save()
    myadmin = Client()
    myadmin.login(username=peter.email, password="default")
    return myadmin

@pytest.mark.parametrize("input,expected", [
    (admin, True),
    (eestecer, False),
])
@pytest.mark.django_db
def test_public_serializer(input, expected):
    baseline = BaseEventFactory.create()
    client = input()
    response = client.get(reverse_lazy("baseevent-detail",kwargs={"pk":baseline.pk}))
    data = json.loads(response.content)
    assert expected == ("group_set" in data)
@pytest.mark.django_db
def test_list_serializer():
    baseline = BaseEventFactory.create()
    client = eestecer()
    response = client.get(reverse_lazy("baseevent-list"))
    data = json.loads(response.content)[0]
    assert all(["pk" in data,"images" in data, "name" in data,"organizing_committee" in data])

class TestBaseEvent(RESTCase, TestCase, AuditCase, ImageCase):
    def setUp(self):
        self.object = BaseEventFactory()
        self.serializer_class = Detail
        super(TestBaseEvent, self).setUp()

    def test_reports_in_generated_data(self):
        r = ReportFactory()
        e = r.content_object
        json = JSONRenderer().render(self.serializer_class(e).data)
        self.assertIn("Organizer Report", json)
    def test_applications_work(self):
        k = AccountFactory(email="asdj@sadjo.de")
        p = ParticipationFactory(user=k, group=self.object.officials)
        self.assertFalse(p.user in self.object.participants)
        self.assertFalse(p in self.object.participations)
        self.assertTrue(p.user in self.object.applicants)
        self.assertTrue(p in self.object.applications)
        for c in p.confirmation_set.all():
            c.confirm()
        self.assertFalse(p.user in self.object.applicants)
        self.assertFalse(p in self.object.applications)
        self.assertTrue(p.user in self.object.participants)
        self.assertTrue(p in self.object.participations)
    def test_organizers_can_modify_event(self):
        p = ParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_baseevent', self.object))
    def test_list_events(self):
        self.assert_retrieve(reverse_lazy('baseevent-list'))

    def test_participation_has_application(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.application)

    def test_participation_has_feedback(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.feedback)

    def test_applicant_can_modify_application(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.user.has_perm('change_response', p.application))

    def test_participant_can_modify_feedback(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.user.has_perm('change_response', p.feedback))


class TestParticipationConfirmation(TestCase):
    def setUp(self):
        self.p = ParticipationConfirmationFactory()
        super(TestParticipationConfirmation, self).setUp()

    def test_polymorphic(self):
        self.assertTrue(self.p in Confirmable.objects.all())
        self.assertTrue(self.p in Confirmation.objects.all())

    def test_accept_participant(self):
        for c in self.p.confirmation_set.all():
            c.confirm()
        self.assertTrue(self.p.confirmed)


class TestExchange(RESTCase, TestCase, AuditCase):
    def setUp(self):
        self.object = ExchangeFactory()
        self.serializer_class = detail_factory(Exchange)
        super(TestExchange, self).setUp()


class TestTraining(RESTCase, TestCase, AuditCase):
    def setUp(self):
        self.object = TrainingFactory()
        self.serializer_class = detail_factory(Training)
        super(TestTraining, self).setUp()


class TestWorkshop(RESTCase, TestCase, AuditCase):
    def setUp(self):
        self.object = WorkshopFactory()
        self.serializer_class = detail_factory(Workshop)
        super(TestWorkshop, self).setUp()

    def test_organizers_can_modify_event(self):
        p = WorkshopParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_workshop', self.object))


class TestTravel(RESTCase, TestCase):
    def setUp(self):
        self.object = TravelFactory()
        self.serializer_class = TravelSerializer
        super(TestTravel, self).setUp()

    def test_organizers_can_view(self):
        self.assertTrue(
            'view_' + self.object._meta.object_name.lower() in get_perms(
                self.object.participation.package.applicable.organizers, self.object))

    def test_user_has_perms(self):
        self.assertTrue(
            self.object.participation.user.has_perm(
                'view_' + self.object._meta.object_name.lower(),
                self.object))
        self.assertTrue(
            self.object.participation.user.has_perm(
                'change_' + self.object._meta.object_name.lower(),
                self.object))

