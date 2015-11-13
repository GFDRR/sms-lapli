__author__ = 'jbjeanniton'

from django.conf.urls import include, url, patterns

urlpatterns = patterns('hydromet.views',
    #url(r'^$', 'home'),
    url(r'^map_overview/$', 'map_overview'),
    url(r'^chart_overview/$', 'chart_overview'),
)


