# -*- coding: utf-8 -*-
import factory

from apps.accounts.factories import ParticipationFactory

from apps.questionnaires.models import Questionnaire, Question, Response, Answer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionnaireFactory(factory.DjangoModelFactory):
    class Meta:
        model = Questionnaire

    name = "feedback"
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


class AnswerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Answer

    response = factory.SubFactory('apps.questionnaires.factories.ResponseFactory')
    answer = "BIG FAT LIE"
    question = factory.SubFactory(QuestionFactory)


class ResponseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Response
        django_get_or_create = ('participation', 'name')

    participation = factory.SubFactory(ParticipationFactory)
    name = factory.Sequence(lambda x: "response " + str(x))

    @factory.post_generation
    def create_responses(self, bla, blabla):
        for i in range(5):
            AnswerFactory(response=self)

