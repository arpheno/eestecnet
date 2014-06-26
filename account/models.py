from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models


class EestecerManager(BaseUserManager):
    """ A manager taking care of creating :class:`Eestecer`objects. """
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
    ('kosher', 'Kosher'),
    ('halal', 'Halal'),
    ('nopork', 'No Pork'),
    ('nofish', 'Pescarian'),
    ('veggie', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('insects', 'Only Insects'),
    ('fruit', 'Fruitarian'),
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
    """email adress"""
    skype = models.CharField(_('Skype Account'), max_length=30, null=True, blank=True)
    """Skype contact info."""
    hangouts = models.CharField(_('Google Hangouts account'), max_length=30, null=True,
                                blank=True)
    """Hangouts contact info"""
    mobile = models.CharField(_('Mobile Phone Number'), max_length=30, null=True,
                              blank=True,
                              help_text=_(
                                  'Please provide your phone number in +XX XXX XXXXXX format'))
    """Mobile Phone number of the user. Mostly used for contact during events."""
    #Personal Information
    first_name = models.CharField(_('first name'), max_length=30)
    """First name"""
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    """First name"""
    last_name = models.CharField(_('last name'), max_length=30)
    """Last name """
    second_last_name = models.CharField(_('second clast name'), max_length=30, blank=True)
    """Last name """
    date_of_birth = models.DateField(blank=True,null=True)
    """ Date of birth"""
    profile_picture = models.ImageField(upload_to="users", blank=True, null=True)
    """A profile picture to be used on the website. Without a Profile picture the user will not appear in lists"""
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    "Gender of the applicant. Useful for overview on Gender balance."
    tshirt_size = models.CharField(max_length=15, choices=TSHIRT_SIZE)
    """T-shirt size. Used for events"""
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    """Passport number required by many hostels. Makes it easier for organizers."""
    food_preferences = models.CharField(max_length=15, choices=FOOD_CHOICES,
                                        default='none')
    """ Food preferences, for example vegetarian or no pork. """
    #EESTEC information
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    """Should be set by the user to the time they joined eestec. For new users it will be the moment they register with the website"""
    def events_participated(self):
        """ Returns the number of :class:`Events <Event>` a :class:`User <account.models.Eestecer>` has been to"""
        try:
            ownevents = self.events.all()
            return len(ownevents)
        except:
            return 0

    def last_event(self):
        """ Returns the Date of the last :class:`Event` a :class:`User <account.models.Eestecer>` has been to"""
        try:
            ownevents = self.events.all()
            if ownevents:
                return self.events.all().order_by('-start_date')[0].start_date
        except:
            return 0


    #Django information
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin site.'))
    """Designates whether the user can log into this admin site"""
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as '
                                        'active. Unselect this instead of deleting accounts.'))
    """Designates whether this user should be treated as active. Unselect this instead of deleting accounts"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','gender']

    objects = EestecerManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together=(('first_name','middle_name','last_name'),)

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s %s %s' % (self.first_name.capitalize(),
                               self.middle_name.capitalize(),
                               self.last_name.capitalize(),
                               self.second_last_name.capitalize())
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return '%s %s' % (self.first_name,self.last_name)
    def __unicode__(self):
        return self.get_full_name()

class Position(models.Model):
    name=models.CharField(max_length=40,unique=True)
    description=models.TextField()

class Achievement(models.Model):
    person = models.ForeignKey(Eestecer,related_name='achievements')
    position= models.ForeignKey(Position)