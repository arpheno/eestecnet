from django.conf.urls import patterns, url

from apps.account.views import EestecerList, EestecerProfile, TrainingList
from apps.account.views import EestecerUpdate


urlpatterns = patterns(
    '',
    url(r'^/?$', EestecerList.as_view(), name='people'),
    url(r'^/me/?$', EestecerUpdate.as_view(), name='userupdate'),
    url(r'^/(?P<slug>[-\w]+)/?$', EestecerProfile.as_view(), name='user'),
    url(r'^/(?P<slug>[-\w]+)/certificate/?$', TrainingList.as_view(),
        name='certificate'),
)
