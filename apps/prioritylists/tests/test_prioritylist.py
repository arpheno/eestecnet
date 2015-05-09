from django.test import TestCase

from apps.accounts.factories import AccountFactory, ParticipationFactory
from apps.events.factories import BaseEventFactory

from apps.prioritylists.factories import PriorityListFactory
from apps.prioritylists.models import PriorityList
from apps.teams.factories import CommitmentFactory
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestPriorityList(RESTCase, TestCase):
    def setUp(self):
        self.object = PriorityListFactory()

    def test_prioritylist_created(self):
        c = CommitmentFactory()
        u = AccountFactory()
        e = BaseEventFactory()
        ParticipationFactory(group=c.members, user=u)
        p = ParticipationFactory(group=e.object.officials, user=u)
        self.assertTrue(PriorityList.objects.get(event=p.package.applicable,
                                                 commitment=p.user.commitment))

    def test_sending_lc_can_modify_prioritylist(self):
        c = CommitmentFactory()
        u = AccountFactory()
        e = BaseEventFactory()
        ParticipationFactory(group=c.members, user=u)
        ParticipationFactory(group=c.board, user=u)
        p = ParticipationFactory(group=e.officials, user=u)
        pl = PriorityList.objects.get(event=p.package.applicable,
                                      commitment=p.user.commitment)
        self.assertTrue(u.has_perm('change_prioritylist', pl))



