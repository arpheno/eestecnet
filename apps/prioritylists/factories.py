# -*- coding: utf-8 -*-
import factory

from apps.prioritylists.models import PriorityList, Priority


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class PriorityListFactory(factory.DjangoModelFactory):
    class Meta:
        model = PriorityList


class PriorityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Priority



