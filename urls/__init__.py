from django.conf.urls.defaults import *
from views import home

urlpatterns = patterns('',
    (r'^$',             home.index),
    (r'^about$',        home.about),
    (r'^feedback$',     home.feedback),
    
    (r'^themes/',       include('urls.themes')),
)
