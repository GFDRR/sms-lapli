__author__ = 'rpalexis'
from django.conf.urls import include, url, patterns
from django.contrib import admin
urlpatterns = patterns('rapport.views',
    #url(r'^$', 'home'),
    url(r'^pluviometrie/$', 'pluviometrie'),
)
