from django.conf.urls import patterns, url
from django.contrib import admin

from apps.feedback.views import NewQuestionset


admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^/feedback/?$',pass),
    url(r'^/feedback/create/?$', NewQuestionset.as_view(), name='newquestionset'),
)
