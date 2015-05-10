from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey, TextField, CharField
from polymorphic import PolymorphicModel

from apps.accounts.models import Account
from common.models import Applicable
from common.util import Reversable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Questionnaire(PolymorphicModel):
    """ Questionnaires store information about Questions that Event organizers would like
    to ask their (potential) participants. """
    group = ForeignKey('accounts.Group')
    name = CharField(max_length=300)


class Question(PolymorphicModel, Reversable):
    """ Questions appear as atoms in Questionnaires """
    questionnaire = ForeignKey('questionnaires.Questionnaire')
    question = TextField()


class Response(PolymorphicModel, Reversable):
    """ Responses store answers to questionnaires"""
    participation = ForeignKey('accounts.Participation')
    name = CharField(max_length=300)


class Answer(PolymorphicModel, Reversable):
    """ Answers appear as atoms in Responses."""
    response = ForeignKey('questionnaires.Response')
    answer = TextField()
    question = ForeignKey('questionnaires.Question')
