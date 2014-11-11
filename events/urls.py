from django.conf.urls import patterns, url
from django.contrib import admin

from events.views import EventDetail, ApplyToEvent, InternationalEvents, confirm_event, \
    FillInTransport, UpdateTransport, ChangeDescription, ChangeDetails, EventImages, \
    AddEvents


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', InternationalEvents.as_view(), name='events'),
    url(r'^add/*$', AddEvents.as_view(), name='batch_add_events'),
    url(r'^(?P<slug>[-\w]+)/*$', EventDetail.as_view(), name='event'),
    url(r'^(?P<slug>[-\w]+)/apply/*', ApplyToEvent.as_view(), name='eventapplication'),
    url(r'^(?P<slug>[-\w]+)/confirm/*$', confirm_event, name='eventconfirmation'),
    url(r'^(?P<slug>[-\w]+)/description/*$',
        ChangeDescription.as_view(), name='eventdescription'),
    url(r'(?P<slug>[-\w]+)/images/*$', EventImages.as_view(),
        name='eventimages'),
    url(r'^(?P<slug>[-\w]+)/transportation/*$', FillInTransport.as_view(),
        name='eventtransportation'),
    url(r'^(?P<slug>[-\w]+)/transportation/update/*', UpdateTransport.as_view(),
        name='updatetransportation'),
    url(r'^(?P<slug>[-\w]+)/details/*$', ChangeDetails.as_view(),
        name='eventchangedetails'),
)
