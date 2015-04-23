# -*- coding: utf-8 -*-
import factory

from apps.events.models import BaseEvent, Workshop, Exchange


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class BaseEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = BaseEvent

    name = "base_event"


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


class ParticipationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'events.Participation'

    user = factory.SubFactory('apps.accounts.factories.AccountFactory')
    package = factory.SubFactory('apps.events.factories.PackageFactory')


class PackageFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'events.Package'

    name = "Wtf"
    event = factory.SubFactory('apps.events.factories.BaseEventFactory')

    @factory.post_generation
    def create_participations(self, bla, blabla):
        return
        for i in range(5):
            ParticipationFactory(package=self)


class QuestionnaireFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'events.Questionnaire'

    package = factory.SubFactory('apps.events.factories.PackageFactory')
    question_one = factory.RelatedFactory('apps.events.factories.QuestionFactory',
                                          'questionnaire')
    question_two = factory.RelatedFactory('apps.events.factories.QuestionFactory',
                                          'questionnaire')


class QuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'events.Question'

    questionnaire = factory.SubFactory('apps.events.factories.QuestionnaireFactory')
    question = "You talking to me?"
