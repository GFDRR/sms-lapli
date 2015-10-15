__author__ = 'rpalexis'
from django.conf.urls import include, url, patterns
from django.contrib import admin
urlpatterns = patterns('public.views',
    #url(r'(?P<age>[0-9]+)', 'home'),
    url(r'', 'acc'),
    url(r'pluviometrie/', 'rpluie'),
    url(r'json_rap/', 'json_rap'),
    url(r'json_graph/', 'json_graph'),
    url(r'json_map/$', 'json_map'),
    url(r'pluviometrie/station_map/$', 'station_map'),
)
