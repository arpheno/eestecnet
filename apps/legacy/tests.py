# -*- coding: utf-8 -*-
import ijson
import pytest

from apps.accounts.factories import AccountFactory
from apps.events.factories import BaseEventFactory
from apps.legacy.account.factories import LegacyAccountFactory
from apps.legacy.account.serializers import LegacyAccountSerializer, \
    ConversionAccountSerializer
from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from common.models import Image


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def convert(data, conversion_map):
    data[None] = None
    dellist = [key for key in conversion_map]
    update = {conversion_map[key]: data[key] for key in conversion_map}
    data.update(update)
    for key in dellist:
        del data[key]
    del data[None]
    return data




