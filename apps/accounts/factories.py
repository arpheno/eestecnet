# -*- coding: utf-8 -*-
import factory

from apps.accounts.models import Account


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account

    first_name = u"Łukasz"
    middle_name = u"Matteusz"
    last_name = u"Knüppel"
    second_last_name = u"Goméz"
    email = factory.sequence(lambda x: "a@b.de" + str(x))


class ParticipationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'accounts.Participation'
        django_get_or_create = ('group',)

    user = factory.SubFactory('apps.accounts.factories.AccountFactory')
    group = factory.SubFactory('apps.accounts.factories.GroupFactory')


class GroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'accounts.Group'
        django_get_or_create = ('name',)

    name = factory.sequence(lambda x: str(x))
    applicable = factory.SubFactory('apps.events.factories.BaseEventFactory')

    @factory.post_generation
    def create_participations(self, bla, blabla):
        for i in range(5):
            ParticipationFactory(group=self)
