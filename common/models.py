from django.db.models import CharField, DateField, BooleanField, ForeignKey, TextField, \
    AutoField
from polymorphic import PolymorphicModel

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
class Confirmable(PolymorphicModel):
    """
    Confirmables have two states: Confirmed(Approved) or pending.
    """
    confirmable_identifier = AutoField(primary_key=True)
    confirmed = BooleanField(default=False, editable=False)

    def on_confirm(self):
        pass

    def check_confirm(self):
        """
        Called by a confirmable's confirmations when they are confirmed. If all
        pending confirmations for the object are resolved, set the confirmed attribute
        to True and save. Classes derived from this class may implement on_confirm to
        run custom actions upon confirmation.
        """
        if all(confirmation.status for confirmation in self.confirmation_set.all()):
            self.on_confirm()
            self.confirmed = True
        else:
            self.confirmed = False
        self.save()


class Notification(PolymorphicModel):
    """
    Notifications prompt users for action
    """
    description = TextField(blank=True, null=True)


class Confirmation(Notification):
    """
    A model that represents the approval of another object by a party,
    which might be a group of users or a user.
    """
    requested = DateField(auto_now=True)
    status = BooleanField(default=False)
    # Because of a bug in django this needs to be deactivated on the first
    # makemigrations call and put in a separate call

    # author = ForeignKey('accounts.Account', null=True, blank=True)
    confirmable = ForeignKey('common.Confirmable')

    def confirm(self):
        self.status = True
        self.save()
    def save(self, *args, **kwargs):
        """
        When a confirmation is saved it should notify its parent about potential changes.
        """
        result = super(Confirmation, self).save(*args, **kwargs)
        self.confirmable.check_confirm()
        return result

class Applicable(Confirmable):
    """
    Basic model that can have groups of users and accepts applications to those groups.
    """
    name = CharField(max_length=50, unique=True)
    def get_absolute_url(self):
        raise NotImplementedError("Child classes have to implement get_absolute_url")


