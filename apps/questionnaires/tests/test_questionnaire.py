from django.test import TestCase
from guardian.shortcuts import get_perms

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
        self.object = QuestionnaireFactory()
        self.serializer_class = QuestionnaireSerializer
        super(TestQuestionnaire, self).setUp()


class TestQuestion(RESTCase, TestCase):
    def setUp(self):
        self.object = QuestionFactory()
        self.serializer_class = QuestionSerializer
        super(TestQuestion, self).setUp()


class TestResponse(RESTCase, TestCase):
    def setUp(self):
        self.object = ResponseFactory()
        self.serializer_class = ResponseSerializer
        super(TestResponse, self).setUp()

    def test_organizers_can_view(self):
        self.assertTrue(
            'view_' + self.object._meta.object_name.lower() in get_perms(
                self.object.participation.package.applicable.organizers, self.object))
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
        self.object = AnswerFactory()
        self.serializer_class = AnswerSerializer
        super(TestAnswer, self).setUp()


    def test_organizers_can_view(self):
        self.assertTrue(
            'view_' + self.object._meta.object_name.lower() in get_perms(
                self.object.response.participation.package.applicable.organizers,
                self.object))

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


