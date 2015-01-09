import datetime

from django.contrib.auth.forms import AuthenticationForm
from haystack.forms import SearchForm

from apps.events.views import featuredevent
from apps.pages.models import WebsiteFeedback, Stub
from apps.pages.views import WebsiteFeedbackForm, WebsiteFeedbackInline


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


def my_feedback(request):
    form = WebsiteFeedbackForm()
    feedback = WebsiteFeedback()
    inlines = [
        WebsiteFeedbackInline(WebsiteFeedback, request, feedback).construct_formset()]
    return {'feedbackform': form, 'feedbackinlines': inlines}

def my_search(request):
    form = SearchForm()
    activities = Stub.objects.filter(group="activities")
    about = Stub.objects.filter(group="about")
    return {'mysearchform': form, "activitystubs": activities, "aboutstubs": about}