# -*- coding: utf-8 -*-
import factory

from common.models import Confirmable, Notification, Confirmation, Applicable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)




class NotificationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Notification

    description = "This is not a description."


class ConfirmationFactory(NotificationFactory):
    class Meta:
        model = Confirmation

    confirmable = factory.SubFactory('common.factories.ConfirmableFactory')


class ApplicableFactory(NotificationFactory):
    class Meta:
        model = Applicable
        django_get_or_create = ('name',)

    name = factory.sequence(lambda x: "applicable" + str(x))


class ConfirmableFactory(factory.DjangoModelFactory):
    class Meta:
        model = Confirmable

    @factory.post_generation
    def create_confirmations(self, bla, blabla):
        for i in range(2):
            ConfirmationFactory(confirmable=self)

