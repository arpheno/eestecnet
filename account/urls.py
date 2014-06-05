from django.conf.urls import patterns, url
from views import  auth, out, new
urlpatterns = patterns('',
                       url(r'^login/', auth, name='login'),
                       url(r'^logout/', out, name='logout'),
                       url(r'^register/', new, name='register'),
                       )
