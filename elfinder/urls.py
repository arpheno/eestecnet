from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required

from views import ElfinderConnectorView, index, connector


urlpatterns = patterns('',
    url(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$',
        staff_member_required(ElfinderConnectorView.as_view()),
        name='yawdElfinderConnectorView'),
    url(r'^$', index, name='materials'),
    url(r'^connector/$', connector, name="trtconnector"),
)