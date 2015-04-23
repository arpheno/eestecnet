# -*- coding: utf-8 -*-
import factory

from apps.accounts.models import Account


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account

    first_name = "Łukasz"
    middle_name = "Matteusz"
    last_name = "Knüppel"
    second_last_name = "Goméz"
    email = "anon@email.com"
