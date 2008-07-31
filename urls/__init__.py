from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^themes/',       include('urls.themes')),
)
