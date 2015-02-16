from django.conf.urls import patterns, url
from django.contrib import admin

from apps.teams.views import SelectBoard, ChangeDescription, \
    ChangeDetails, ManageMembers, TeamImages, TeamApplications, OutgoingApplications, \
    TeamDetail


admin.autodiscover()
# Serializers define the API representation.

# ViewSets define the view behavior.
# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = patterns(
    '',
    url(r'^/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='detail'),
    url(r'^/(?P<slug>[-\w]+)/board/?$', SelectBoard.as_view(), name='board'),
    url(r'^/(?P<slug>[-\w]+)/description/?$', ChangeDescription.as_view(),
        name='description'),
    url(r'(?P<slug>[-\w]+)/images/?$', TeamImages.as_view(), name='teamimages'),
    url(r'(?P<slug>[-\w]+)/outgoing/?', OutgoingApplications.as_view(),
        name='outgoing'),
    url(r'(?P<slug>[-\w]+)/applications/?', TeamApplications.as_view(),
        name='teamapplications'),
    url(r'^/(?P<slug>[-\w]+)/members/?$', ManageMembers.as_view(), name='managemembers'),
    url(r'^/(?P<slug>[-\w]+)/details/?$', ChangeDetails.as_view(), name='changedetails'),
)
