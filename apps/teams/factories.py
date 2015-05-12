# -*- coding: utf-8 -*-
import factory

from apps.accounts.factories import AccountFactory

from apps.teams.models import Commitment, InternationalTeam, BaseTeam


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class BaseTeamFactory(factory.DjangoModelFactory):

    class Meta:
        model = BaseTeam
        django_get_or_create = ['name']

    name = "Amsterdam"
    owner = factory.SubFactory(AccountFactory)

class CommitmentFactory(BaseTeamFactory):
    class Meta:
        model = Commitment
        django_get_or_create = ['name']

    name = "Amsterdam"


class InternationalTeamFactory(BaseTeamFactory):
    class Meta:
        model = InternationalTeam

    name = "IT Team"
