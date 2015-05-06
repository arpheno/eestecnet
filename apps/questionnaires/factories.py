# -*- coding: utf-8 -*-
import factory

from apps.questionnaires.models import Questionnaire, Question


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionnaireFactory(factory.DjangoModelFactory):
    class Meta:
        model = Questionnaire

    group = factory.SubFactory('apps.accounts.factories.GroupFactory')
    question_one = factory.RelatedFactory(
        'apps.questionnaires.factories.QuestionFactory',
        'questionnaire')
    question_two = factory.RelatedFactory(
        'apps.questionnaires.factories.QuestionFactory',
        'questionnaire')


class QuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Question
        django_get_or_create = ('questionnaire', 'question')

    questionnaire = factory.SubFactory(QuestionnaireFactory)
    question = "You talking to me?"

