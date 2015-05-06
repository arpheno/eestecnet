from django.core.urlresolvers import reverse_lazy

from django.test import TestCase, Client

from apps.accounts.factories import ParticipationFactory, AccountFactory

from apps.events.factories import BaseEventFactory, ParticipationConfirmationFactory, \
    ExchangeFactory, TrainingFactory, WorkshopFactory, WorkshopParticipationFactory
from apps.prioritylists.models import PriorityList
from apps.teams.factories import CommitmentFactory
from common.models import Confirmable, Confirmation
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestBaseEvent(TestCase, RESTCase):
    def setUp(self):
        self.object = BaseEventFactory()
        self.c = Client()

    def test_organizers_can_modify_event(self):
        p = ParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_baseevent', self.object))

    def test_list_events(self):
        self.assert_retrieve(reverse_lazy('baseevent-list'))

    def test_applicant_can_modify_application(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.user.has_perm('change_questionnaire', p.package.application))

    def test_participant_can_modify_feedback(self):
        p = ParticipationFactory(group=self.object.officials)
        self.assertTrue(p.user.has_perm('change_response', p.package.feedback))

    def test_prioritylist_created(self):
        c = CommitmentFactory()
        u = AccountFactory()
        ParticipationFactory(group=c.members, user=u)
        p = ParticipationFactory(group=self.object.officials, user=u)
        self.assertTrue(PriorityList.objects.get(event=p.package.applicable,
                                                 commitment=p.user.commitment))


class TestParticipationConfirmation(TestCase):
    def setUp(self):
        self.p = ParticipationConfirmationFactory()

    def test_polymorphic(self):
        self.assertTrue(self.p in Confirmable.objects.all())
        self.assertTrue(self.p in Confirmation.objects.all())

    def test_accept_participant(self):
        for c in self.p.confirmation_set.all():
            c.confirm()
        self.assertTrue(self.p.confirmed)

    def test_confirm_participation(self):
        for c in self.p.confirmation_set.all():
            c.confirm()
        self.assertTrue(self.p.confirmed)
        self.p.confirm()
        self.assertTrue(self.p.confirmable.confirmed)


class TestExchange(RESTCase, TestCase):
    def setUp(self):
        self.object = ExchangeFactory()


class TestTraining(RESTCase, TestCase):
    def setUp(self):
        self.object = TrainingFactory()


class TestWorkshop(RESTCase, TestCase):
    def setUp(self):
        self.object = WorkshopFactory()

    def test_organizers_can_modify_event(self):
        p = WorkshopParticipationFactory(group=self.object.organizers)
        self.assertTrue(p.user.has_perm('change_workshop', self.object))