from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models import EmailField, CharField

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class Account(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name

    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30)
    last_name = CharField(max_length=40)
    second_last_name = CharField(max_length=40)
    email = EmailField()

