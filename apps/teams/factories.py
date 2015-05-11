# -*- coding: utf-8 -*-
import factory

from apps.teams.models import Commitment, InternationalTeam


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CommitmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Commitment
        django_get_or_create = ['name']

    name = "Amsterdam"


class InternationalTeamFactory(factory.DjangoModelFactory):
    class Meta:
        model = InternationalTeam

    name = "IT Team"
