from django.contrib.auth.forms import AuthenticationForm
from account.views import Login
from events.views import featuredevent


import datetime

def date_now(request):
    return {'date_now':datetime.datetime.now()}
def login_processor(request):
    form=AuthenticationForm()
    return {'loginform':form}
def random_event_processor(request):
    try:
        return {'featuredevent':featuredevent()}
    except:
        return {'None':None}