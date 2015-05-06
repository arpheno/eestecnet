from django.contrib import auth
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, \
    PermissionsMixin, Permission, _user_get_all_permissions, _user_has_perm, \
    _user_has_module_perms, GroupManager
from django.core.urlresolvers import reverse
from django.db.models import EmailField, CharField, BooleanField, ManyToManyField, \
    ForeignKey
from django.utils.translation import ugettext_lazy as _
from guardian.mixins import GuardianUserMixin
from polymorphic import PolymorphicModel

from apps.teams.models import Commitment
from common.models import Confirmable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

objects = GroupManager()


class Group(auth.models.Group):
    """
     An applicable can have different groups, which relate users to it.
    """
    applicable = ForeignKey('common.Applicable', related_name='packages')
    objects = GroupManager()
    test = CharField(default="LOL", max_length=100)

    @property
    def application(self):
        return self.response_set.get(name="application")

    @property
    def feedback(self):
        return self.response_set.get(name="feedback")

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('group-detail',kwargs={'pk': self.pk})
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')



# Create your models here.
class Account(GuardianUserMixin, AbstractBaseUser):
    is_superuser = BooleanField(_('superuser status'), default=False,
                                help_text=_(
                                    'Designates that this user has all permissions '
                                    'without '
                                    'explicitly assigning them.'))
    groups = ManyToManyField('auth.Group', verbose_name=_('groups'),
                             blank=True,
                             through='accounts.Participation',
                             help_text=_('The groups this user belongs to. A user will '
                                         'get all permissions granted to each of '
                                         'their groups.'),
                             related_name="user_set", related_query_name="user")
    user_permissions = ManyToManyField(Permission,
                                       verbose_name=_('user permissions'), blank=True,
                                       help_text=_(
                                           'Specific permissions for this user.'),
                                       related_name="user_set",
                                       related_query_name="user")

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
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name

    @property
    def commitment(self):
        return self.participation_set.get(
            group__name__endswith="members").package.applicable


    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30, blank=True, null=True)
    last_name = CharField(max_length=40)
    second_last_name = CharField(max_length=40, blank=True, null=True)
    email = EmailField(unique=True)
    def get_absolute_url(self):
        return reverse('account-detail',kwargs={'pk': self.pk})


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
        super(Participation, self).save(**kwargs)
    def get_absolute_url(self):
        return reverse('participation-detail',kwargs={'pk':self.pk,'group_pk':self.group.pk})

