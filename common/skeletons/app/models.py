from django.contrib.auth.models import User

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class Account(User):
    pass