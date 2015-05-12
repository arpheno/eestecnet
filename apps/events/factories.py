# -*- coding: utf-8 -*-
import factory

from apps.accounts.factories import AccountFactory

from apps.events.models import BaseEvent, Workshop, Exchange, ParticipationConfirmation


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class BaseEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = BaseEvent
        django_get_or_create = ['name']

    name = "base_event"
    owner = factory.SubFactory(AccountFactory)


class WorkshopFactory(BaseEventFactory):
    class Meta:
        model = Workshop

    name = "Inktronics"


class ExchangeFactory(BaseEventFactory):
    class Meta:
        model = Exchange

    name = "Jahorina Spring Break"


class TrainingFactory(BaseEventFactory):
    class Meta:
        model = BaseEvent

    name = "Emotional Intelligence"




class WorkshopParticipationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'accounts.Participation'

    group = factory.SubFactory('apps.events.factories.WorkshopPackageFactory')
    user = factory.SubFactory('apps.accounts.factories.AccountFactory')


class ParticipationConfirmationFactory(factory.DjangoModelFactory):
    class Meta:
        model = ParticipationConfirmation

    confirmable = factory.SubFactory(WorkshopParticipationFactory)
class WorkshopPackageFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'accounts.Group'

    applicable = factory.SubFactory('apps.events.factories.WorkshopFactory')


