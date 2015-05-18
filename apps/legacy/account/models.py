from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser)


FIELDS_OF_STUDY = (
    ("ee", "Electrical Engineering"),
    ("it", "Information Technology"),
    ("cs", "Computer Science"),
    ("bm", "Biomedical Engineering"),
    ("tc", "Telecommunications"),
    ("pe", "Power Engineering"),
    ("se", "Software Engineering"),
    ("au", "Automatics"),
    ("ns", "Natural Sciences"),
    ("ss", "Social Sciences"),
    ("ec", "Economy"),
    ("oe", "Other engineering subjects"),
    ("oo", "Other"),
)
FOOD_CHOICES = (
    ('none', 'None'),
    ('kosher', 'Kosher'),
    ('halal', 'Halal'),
    ('nopork', 'No Pork'),
    ('nofish', 'Pescarian'),
    ('veggie', 'Vegetarian'),
    ('vegan', 'Vegan'),
)
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'), ('x', 'Other'), )
TSHIRT_SIZE = (('mxs', 'Male XS'), ('ms', 'Male S'), ('mm', 'Male M'), ('ml', 'Male L'),
               ('mxl', 'Male XL'), ('mxxl', 'Male XXL'), ('mxxxl', 'Male XXXL'),
               ('fxs', 'Female XS'), ('fs', 'Female S'), ('fm', 'Female M'),
               ('fl', 'Female L'), ('fxl', 'Female XL'), ('fxxl', 'Female XXL'),
               ('fxxxl', 'Female XXXL'), )


def get_eestecer_slug(instance):
    if instance.middle_name:
        return "%s-%s-%s" % (
            instance.first_name, instance.middle_name, instance.last_name)
    else:
        return "%s-%s-%s" % (
            instance.first_name, instance.middle_name, instance.last_name)


class Eestecer(AbstractBaseUser):
    # Basic Information
    def name(self):
        return self.get_full_name()

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email

    thumbnail = models.ImageField(upload_to="users", null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from=get_eestecer_slug)
    #Contact information
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    skype = models.CharField(_('Skype Account'), max_length=30, null=True, blank=True)
    hangouts = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(_('Mobile Phone Number'), max_length=30, null=True,
                              blank=True,
                              help_text=_(
                                  'Please provide your phone number in +XX XXX XXXXXX '
                                  'format'))
    #Names
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30)
    second_last_name = models.CharField(_('second last name'), max_length=30, blank=True)
    """ For our friends from the iberic peninsula"""
    date_of_birth = models.DateField(blank=True, null=True)
    show_date_of_birth = models.BooleanField(default=True)
    receive_eestec_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    tshirt_size = models.CharField(max_length=15, choices=TSHIRT_SIZE, blank=True,
                                   null=True)
    allergies = models.CharField(max_length=50, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    activation_link = models.CharField(max_length=50, blank=True, null=True)
    """Passport number required by many hostels. Makes it easier for organizers."""
    field_of_study = models.CharField(max_length=50, choices=FIELDS_OF_STUDY)
    food_preferences = models.CharField(max_length=15, choices=FOOD_CHOICES,
                                        default='none')
    """ Food preferences, for example vegetarian or no pork. """
    curriculum_vitae = models.FileField(upload_to="cvs", blank=True, null=True)
    """ For the future incorporation of Lykeion """
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    """Should be set by the user to the time they joined eestec. For new users it will
    be the moment they register with the website"""
    #Django information
    is_staff = models.BooleanField(_('active'), default=False)
    is_active = models.BooleanField(_('active'), default=True)


    #
    # class Position(models.Model):
    #     name = models.CharField(max_length=60, unique=True)
    #     description = models.TextField()
    #
    #     def __unicode__(self):
    #         return self.name
    #
    #
    # class Achievement(models.Model):
    #     person = models.ForeignKey(Eestecer, related_name='achievements')
    #     position = models.ForeignKey(Position)
    #     member = models.ForeignKey('teams.Team', blank=True, null=True)
    #     date = models.DateField(auto_now_add=True)
    #     event = models.ForeignKey('events.Event', null=True, blank=True)
    #     def __unicode__(self):
    #         return self.person.get_short_name() + " - " + self.position.name