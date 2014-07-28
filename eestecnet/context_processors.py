import datetime

from django.contrib.auth.forms import AuthenticationForm
from haystack.forms import SearchForm

from events.views import featuredevent


def date_now(request):
    return {'date_now': datetime.datetime.now()}


def login_processor(request):
    form = AuthenticationForm()
    return {'loginform': form}


def random_event_processor(request):
    try:
        return {'featuredevent': featuredevent()}
    except:
        return {'None': None}


def my_search(request):
    form = SearchForm()
    return {'mysearchform': form}