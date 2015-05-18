# -*- coding: utf-8 -*-
import datetime

import factory

from apps.legacy.account.models import Eestecer



# -*- coding: utf-8 -*-
__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LegacyAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Eestecer

    tshirt_size = "mxxl"
    passport_number = "asdad"
    # Information important for companies
    field_of_study = "ee"
    first_name = u"Łukasz"
    middle_name = u"Matteusz"
    last_name = u"Knüppel"
    second_last_name = u"Goméz"
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    email = factory.sequence(lambda x: str(x) + "a@b.de" + str(x))
    gender = "m"

    thumbnail = factory.django.ImageField(color="blue")
    description = "description"
    date_of_birth = datetime.datetime.now().date()
    allergies = "allergies"
    activation_link = "activation_link"
    food_preferences = "vegan"
    """ Food preferences, for example vegetarian or no pork. """
    curriculum_vitae = factory.django.FileField(name="lol.txt")
