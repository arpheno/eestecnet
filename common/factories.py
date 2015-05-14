# -*- coding: utf-8 -*-
import factory

from apps.events.factories import BaseEventFactory
from common.models import Confirmable, Notification, Confirmation, Applicable, Image


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


class ApplicableFactory(factory.DjangoModelFactory):
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


class ImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Image

    full_size = factory.django.ImageField(color='blue', width=200, height=200)
    content_object = factory.SubFactory(BaseEventFactory)