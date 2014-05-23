from django.conf.urls import patterns, url
from views import UserProfile, auth, out, new, complete
urlpatterns = patterns('',
                       url(r'^$', UserProfile.as_view(), name="index"),
                       url(r'^login/', auth, name='login'),
                       url(r'^logout/', out, name='logout'),
                       url(r'^new/', new, name='register'),
                       url(r'^complete/(.*)$', complete),
                       )
