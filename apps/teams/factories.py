# -*- coding: utf-8 -*-
import factory

from apps.teams.models import Commitment


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CommitmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Commitment

    name = "Amsterdam"



