__author__ = 'jbjeanniton'

from django.apps import AppConfig


class PrixDuMarcheConfig(AppConfig):
    name = 'prix_marche'
    verbose_name = 'Prix du Marché'

    def ready(self):
        import hydromet.signals