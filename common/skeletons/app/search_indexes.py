from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
from haystack import indexes


class AccountIndex(indexes.SearchIndex, indexes.Indexable):
    ''' Search index for accounts. Currently only searching by full name. '''
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Account
