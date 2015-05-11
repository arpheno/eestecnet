# -*- coding: utf-8 -*-
import factory

from apps.accounts.factories import AccountFactory
from apps.events.factories import BaseEventFactory
from apps.prioritylists.models import PriorityList, Priority
from apps.teams.factories import CommitmentFactory


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class PriorityListFactory(factory.DjangoModelFactory):
    class Meta:
        model = PriorityList

    commitment = factory.SubFactory(CommitmentFactory)
    event = factory.SubFactory(BaseEventFactory)


class PriorityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Priority

    priority_list = factory.SubFactory(PriorityListFactory)
    user = factory.SubFactory(AccountFactory)
    priority = factory.sequence(lambda x: x)



