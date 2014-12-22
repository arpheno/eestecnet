from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import DetailView

from teams.models import Team
from teams.views import SelectBoard, ChangeDescription, \
    ChangeDetails, ManageMembers, TeamImages, TeamApplications


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Team),
                           name='detail'),
                       url(r'^(?P<slug>[-\w]+)/board/*$', SelectBoard.as_view(),
                           name='board'),
                       url(r'^(?P<slug>[-\w]+)/description/*$',
                           ChangeDescription.as_view(), name='description'),
                       url(r'(?P<slug>[-\w]+)/images/*$', TeamImages.as_view(),
                           name='teamimages'),
                       url(r'(?P<slug>[-\w]+)/applications/*',
                           TeamApplications.as_view(),
                           name='teamapplications'),
                       url(r'^(?P<slug>[-\w]+)/members/*$', ManageMembers.as_view(),
                           name='managemembers'),
                       url(r'^(?P<slug>[-\w]+)/details/*$', ChangeDetails.as_view(),
                           name='changedetails'),
)
