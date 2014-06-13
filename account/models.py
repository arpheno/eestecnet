from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models
from events.models import Event


class EestecerManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


FOOD_CHOICES = (
    ('none', 'None'),
    ('nopork', 'No Pork'),
    ('veggie', 'Vegetarian'),
    ('vegan', 'Vegan'),

)
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'), ('x', 'Other'), )
TSHIRT_SIZE = (('mxs', 'Male XS'), ('ms', 'Male S'), ('mm', 'Male M'), ('ml', 'Male L'),
               ('mxl', 'Male XL'), ('mxxl', 'Male XXL'), ('mxxxl', 'Male XXXL'),
               ('fxs', 'Female XS'), ('fs', 'Female S'), ('fm', 'Female M'),
               ('fl', 'Female L'), ('fxl', 'Female XL'), ('fxxl', 'Female XXL'),
               ('fxxxl', 'Female XXXL'), )


class Eestecer(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username. It stores additional information
    about eestecers.

    Email and password are required. Other fields are optional.
    """
    #Contact information
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    """Skype contact info."""
    skype = models.CharField(_('Skype Account'), max_length=30, null=True, blank=True)
    """Hangouts contact info"""
    hangouts = models.CharField(_('Google Hangouts account'), max_length=30, null=True,
                                blank=True)
    """Mobile Phone number of the user. Mostly used for contact during events."""
    mobile = models.CharField(_('Mobile Phone Number'), max_length=30, null=True,
                              blank=True,
                              help_text=_(
                                  'Please provide your phone number in +XX XXX XXXXXX format'))
    #Personal Information
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    """A profile picture to be used on the website. Without a Profile picture the user will not appear in lists"""
    profile_picture = models.ImageField(upload_to="users", blank=True, null=True)
    "Gender of the applicant. Useful for overview on Gender balance."
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    """T-shirt size. Used for events"""
    tshirt_size = models.CharField(max_length=15, choices=TSHIRT_SIZE)
    """Passport number required by many hostels. Makes it easier for organizers."""
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    """ Food preferences, for example vegetarian or no pork. """
    food_preferences = models.CharField(max_length=15, choices=FOOD_CHOICES,
                                        default='none')
    #EESTEC information
    """Should be set by the user to the time they joined eestec. For new users it will be the moment they register with the website"""
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    def events_participated(self):
        try:
            ownevents = self.event_set.all()
            return len(ownevents)
        except:
            return 0

    def last_event(self):
        try:
            ownevents = self.event_set.all()
            if ownevents:
                return self.event_set.all().order_by('-start_date')[0].start_date
            else:
                return 0
        except:
            return 0


    #Django information
    """Designates whether the user can log into this admin site"""
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin site.'))
    """Designates whether this user should be treated as active. Unselect this instead of deleting accounts"""
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as '
                                        'active. Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EestecerManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s%s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
