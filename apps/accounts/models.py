from django.contrib import auth
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, \
    PermissionsMixin, Permission, _user_get_all_permissions, _user_has_perm, \
    _user_has_module_perms, GroupManager, BaseUserManager
from django.contrib.contenttypes.fields import GenericRelation
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models import EmailField, CharField, BooleanField, ManyToManyField, \
    ForeignKey, DateField, FileField, IntegerField
from django.utils.translation import ugettext_lazy as _
from guardian.mixins import GuardianUserMixin
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.help_texts import GROUPS_HELP_TEXT
from apps.accounts.help_texts import IS_SUPERUSER_HELP_TEXT
from apps.teams.models import Commitment
from common.models import Confirmable, Confirmation, DescriptionMixin
from settings.conf.choices import GENDER_CHOICES, TSHIRT_SIZE, FIELDS_OF_STUDY, \
    FOOD_CHOICES


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

objects = GroupManager()


class Group(auth.models.Group):
    """
     An applicable can have different groups, which relate users to it.
    """
    applicable = ForeignKey('common.Applicable')
    objects = GroupManager()
    test = CharField(default="LOL", max_length=100)
    fee = IntegerField(default=0)
    max_participants = IntegerField(default=0)
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        kwargs['email'] = email
        account = self.model(**kwargs)

        print account
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_superuser = True
        account.save()

        return account


# Create your models here.
class AbstractAccount(object):
    def get_group_permissions(self, obj=None):
        """
        Returns a list of permission strings that this user has through their
        groups. This method queries all available auth backends. If an object
        is passed in, only permissions matching this object are returned.
        """
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions


    def get_all_permissions(self, obj=None):
        return _user_get_all_permissions(self, obj)

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission. This method
        queries all available auth backends, but returns immediately if any
        backend returns True. Thus, a user who has permission from a single
        auth backend is assumed to have permission in general. If an object is
        provided, permissions for this specific object are checked.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Account(GuardianUserMixin, AbstractAccount, AbstractBaseUser, DescriptionMixin,
              object):
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_active = BooleanField(_('active'), default=True,
                             help_text=_(
                                 'Designates whether this user should be treated as '
                                 'active. Unselect this instead of deleting accounts.'))
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name

    @property
    def commitment(self):
        # TODO if a user is in two commitments, we only get one of them
        return Commitment.objects.filter(group__user=self)[0]

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'pk': self.pk})

    # Personal information
    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30, blank=True)
    last_name = CharField(max_length=40)
    second_last_name = CharField(max_length=40, blank=True)
    email = EmailField(unique=True)
    birthday = DateField(blank=True, null=True)
    birthday_show = BooleanField(default=True)

    # Information important for events
    images = GenericRelation('common.Image', related_query_name='images')
    tshirt_size = CharField(max_length=15, choices=TSHIRT_SIZE, null=True, blank=True)
    allergies = CharField(max_length=300, null=True, blank=True)
    food_preferences = CharField(max_length=30, choices=FOOD_CHOICES, blank=True)
    passport_number = CharField(max_length=20, null=True, blank=True)
    mobile = CharField(max_length=50, null=True, blank=True)
    skype = CharField(max_length=50, null=True, blank=True)
    hangouts = CharField(max_length=50, null=True, blank=True)
    gender = CharField(max_length=15, choices=GENDER_CHOICES)

    #Information important for companies
    field_of_study = CharField(max_length=50, choices=FIELDS_OF_STUDY, blank=True,
                               null=True)
    curriculum_vitae = FileField(upload_to="currcula_vitae", blank=True, null=True)

    #Information related to the platform
    receive_eestec_active = BooleanField(default=True)
    date_joined = DateField(auto_now_add=True)
    is_superuser = BooleanField(default=False, help_text=IS_SUPERUSER_HELP_TEXT)
    groups = ManyToManyField('auth.Group', blank=True, through='accounts.Participation',
                             help_text=GROUPS_HELP_TEXT,
                             related_name="user_set", related_query_name="user")
    user_permissions = ManyToManyField(Permission, blank=True, related_name="user_set",
                                       null=True,
                                       related_query_name="user")


class Participation(Confirmable):
    """ Participations hold information about the application, the transport,
    and feedback when attending an event."""
    user = ForeignKey(Account)
    group = ForeignKey('auth.Group')

    @property
    def package(self):
        return Group.objects.get(group_ptr_id=self.group.pk)

    def __unicode__(self):
        return str(self.package)

    def save(self, **kwargs):
        if not self.pk:
            result = super(Participation, self).save(**kwargs)
            from apps.events.models import ParticipationConfirmation

            p = ParticipationConfirmation.objects.create(confirmable=self)
            p.save()
            from apps.questionnaires.models import Response

            f = Response.objects.create(participation=self, name="feedback")
            a = Response.objects.create(participation=self, name="application")
            assign_perm('change_response', self.user, f)
            assign_perm('change_response', self.user, a)
        else:
            result = super(Participation, self).save(**kwargs)
        return result

    def get_absolute_url(self):
        return reverse('participation-detail',
                       kwargs={'pk': self.pk, 'group_pk': self.group.pk})

    @property
    def application(self):
        return self.response_set.get(name="application")

    @property
    def feedback(self):
        return self.response_set.get(name="feedback")
