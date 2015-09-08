from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey, TextField, CharField
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account
from common.models import Applicable
from common.util import Reversable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Questionnaire(PolymorphicModel, Reversable):
    """ Questionnaires store information about Questions that Event organizers would like
    to ask their (potential) participants. """
    group = ForeignKey('accounts.Group')
    name = CharField(max_length=300)


class Question(PolymorphicModel, Reversable):
    """ Questions appear as atoms in Questionnaires """
    questionnaire = ForeignKey('questionnaires.Questionnaire')
    question = TextField()
    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Question, self).save()
            label = self._meta.object_name
            assign_perm('view_' + label.lower(),
                        self.questionnaire.group, self)
            assign_perm('view_' + label.lower(),
                        self.questionnaire.group.applicable.organizers, self)
            assign_perm('change_' + label.lower(),
                        self.questionnaire.group.applicable.organizers, self)
        else:
            result = super(Question, self).save()
        return result


class Response(PolymorphicModel, Reversable):
    """ Responses store answers to questionnaires"""
    participation = ForeignKey('accounts.Participation')
    name = CharField(max_length=300)

    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Response, self).save()
            label = self._meta.object_name
            assign_perm('view_' + label.lower(), self.participation.user, self)
            assign_perm('change_' + label.lower(), self.participation.user, self)
            assign_perm('view_' + label.lower(),
                        self.participation.package.applicable.organizers, self)
        else:
            result = super(Response, self).save()
        return result


class Answer(PolymorphicModel, Reversable):
    """ Answers appear as atoms in Responses."""
    response = ForeignKey('questionnaires.Response')
    answer = TextField()
    question = ForeignKey('questionnaires.Question')

    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Answer, self).save()
            label = self._meta.object_name
            assign_perm('change_' + label.lower(), self.response.participation.user,
                        self)
            assign_perm('view_' + label.lower(), self.response.participation.user, self)
            assign_perm('delete_' + label.lower(), self.response.participation.user,
                        self)
            assign_perm('view_' + label.lower(),
                        self.response.participation.package.applicable.organizers, self)
        else:
            result = super(Answer, self).save()
        return result

