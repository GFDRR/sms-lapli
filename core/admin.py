from django.contrib import admin

# Register your models here.
from .models import Departement, Commune, SectionCommunale, SiteSentinelle

admin.site.register(Departement)
admin.site.register(Commune)
admin.site.register(SectionCommunale)
admin.site.register(SiteSentinelle)
