__author__ = 'jbjeanniton'

from django.apps import AppConfig


class HydrometConfig(AppConfig):
    name = 'hydromet'
    verbose_name = 'Hydromet Application'

    def ready(self):
        import hydromet.signals