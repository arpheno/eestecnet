# -*- coding: utf-8 -*-
import datetime

from django.utils.timezone import now
import factory

from apps.accounts.factories import AccountFactory, ParticipationFactory
from apps.events.models import BaseEvent, Workshop, Exchange, \
    ParticipationConfirmation, \
    Travel, Training


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
    deadline = datetime.datetime.now()
    max_participants = 5
    unofficial_fee = 500


class WorkshopFactory(BaseEventFactory):
    class Meta:
        model = Workshop

    name = "Inktronics"
    start_date = datetime.datetime.today().date()
    end_date = datetime.datetime.today().date()
    location = "munich"


class ExchangeFactory(BaseEventFactory):
    class Meta:
        model = Exchange

    name = "Jahorina Spring Break"
    start_date = datetime.datetime.today().date()
    end_date = datetime.datetime.today().date()
    location = "jahorina"
    participation_fee = 500


class TrainingFactory(BaseEventFactory):
    class Meta:
        model = Training

    name = "Emotional Intelligence"
    date = datetime.datetime.today().date()
    location = u"Kraków"


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


class TravelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Travel

    participation = factory.SubFactory(ParticipationFactory)
    arrival_datetime = now()
    departure_datetime = now()
    arrival_mode = 'car'
    departure_mode = 'car'
    comment = "moo"
