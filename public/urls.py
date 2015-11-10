__author__ = 'rpalexis'
from django.conf.urls import include, url, patterns
from django.contrib import admin
urlpatterns = patterns('public.views',
    url(r'^$', 'home'),
    url(r'^accueil/$', 'home'),
    url(r'^faq/$', 'faq'),
    #url(r'pluviometrie/', 'rpluie'),
    #url(r'json_rap/', 'json_rap'),
    #url(r'json_graph/', 'json_graph'),
    #url(r'json_map/$', 'json_map'),
    #url(r'pluviometrie/station_map/$', 'station_map'),
)
