from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Departement)
admin.site.register(Commune)
admin.site.register(SectionCommunale)
admin.site.register(SiteSentinelle)
admin.site.register(Poste)
admin.site.register(PersonneContact)