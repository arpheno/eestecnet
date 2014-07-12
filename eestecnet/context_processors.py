from django.contrib.auth.forms import AuthenticationForm
from account.views import Login
from events.views import featuredevent


def login_processor(request):
    form=AuthenticationForm()
    return {'loginform':form}
def random_event_processor(request):
    try:
        return {'featuredevent':featuredevent()}
    except:
        return {'None':None}