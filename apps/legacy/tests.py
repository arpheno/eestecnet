# -*- coding: utf-8 -*-
import pytest

from apps.legacy.account.factories import LegacyAccountFactory
from apps.legacy.account.serializers import LegacyAccountSerializer, \
    ConversionAccountSerializer
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


@pytest.mark.django_db
def test_convert_account():
    # Legacy side
    with open('media/example.dat', 'wb') as cv:
        cv.write("LOL")
    with open('media/example.jpg', 'wb') as cv:
        with open('media/images/0aa84e03-5f0.jpg', 'rb') as img:
            cv.write(img.read())
    object = LegacyAccountFactory.build(email="asdf@asdf.de")
    object = LegacyAccountFactory.build(email="asdf@asdf.de")
    data = LegacyAccountSerializer(object).data
    serializer = ConversionAccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    account = serializer.save()
    assert account.middle_name == u"Matteusz"
    assert len(Image.objects.all()) == 1
