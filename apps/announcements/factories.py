# -*- coding: utf-8 -*-
import factory

from apps.announcements.models import Announcement, News, CareerOffer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AnnouncementFactory(factory.DjangoModelFactory):
    class Meta:
        model = Announcement

    name = "Short text"
    description = "long text"


class NewsFactory(AnnouncementFactory):
    class Meta:
        model = News


class CareerOfferFactory(AnnouncementFactory):
    class Meta:
        model = CareerOffer