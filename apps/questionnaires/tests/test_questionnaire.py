from django.test import TestCase

from apps.questionnaires.factories import QuestionnaireFactory, QuestionFactory, \
    ResponseFactory, AnswerFactory
from apps.questionnaires.serializers import QuestionnaireSerializer, \
    QuestionSerializer, \
    ResponseSerializer, AnswerSerializer
from common.util import RESTCase


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestQuestionnaire(RESTCase, TestCase):
    def setUp(self):
        super(TestQuestionnaire, self).setUp()
        self.object = QuestionnaireFactory()
        self.serializer_class = QuestionnaireSerializer


class TestQuestion(RESTCase, TestCase):
    def setUp(self):
        super(TestQuestion, self).setUp()
        self.object = QuestionFactory()
        self.serializer_class = QuestionSerializer


class TestResponse(RESTCase, TestCase):
    def setUp(self):
        super(TestResponse, self).setUp()
        self.object = ResponseFactory()
        self.serializer_class = ResponseSerializer

    def test_user_has_perms(self):
        self.assertTrue(
            self.object.participation.user.has_perm(
                'view_' + self.object._meta.object_name.lower(),
                self.object))
        self.assertTrue(
            self.object.participation.user.has_perm(
                'change_' + self.object._meta.object_name.lower(),
                self.object))


class TestAnswer(RESTCase, TestCase):
    def setUp(self):
        super(TestAnswer, self).setUp()
        self.object = AnswerFactory()
        self.serializer_class = AnswerSerializer

    def test_user_has_perms(self):
        self.assertTrue(
            self.object.response.participation.user.has_perm(
                'view_' + self.object._meta.object_name.lower(),
                self.object))
        self.assertTrue(
            self.object.response.participation.user.has_perm(
                'delete_' + self.object._meta.object_name.lower(),
                self.object))
        self.assertTrue(
            self.object.response.participation.user.has_perm(
                'change_' + self.object._meta.object_name.lower(),
                self.object))


