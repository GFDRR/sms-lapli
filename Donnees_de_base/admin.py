from django.contrib import admin

# Register your models here.
from .models import *

class DepartementAdmin(admin.ModelAdmin):
    list_display = ("departement", "description")




class CommuneAdmin(admin.ModelAdmin):
    list_display = ("get_departement", "commune", "description")

    def get_departement(self, instance):
        return instance.departement.departement



class SectionCommunaleAdmin(admin.ModelAdmin):
    list_display = ("commune", "sectionCommunale", "description")



class SiteSentinelleAdmin(admin.ModelAdmin):
    list_display = ("get_sectionCommunale", "localite", "latitude", "longitude", "hauteur")

    def get_sectionCommunale(self, instance):
        return instance.sectionCommunale.sectionCommunale



class PosteAdmin(admin.ModelAdmin):
    list_display = ("nomPoste", "description")



class PersonneContactAdmin(admin.ModelAdmin):
    list_display = ("get_nomPoste", "nomPersonne", "prenomPersonne", "telephoneBureau", "telephonePersonnel", "emailPersonnel", "adressePersonnelle", "nif", "cin", "dateEmbauche")

    def get_nomPoste(self, instance):
        return instance.nomPoste.nomPoste


admin.site.register(Departement, DepartementAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(SectionCommunale, SectionCommunaleAdmin)
admin.site.register(SiteSentinelle, SiteSentinelleAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(PersonneContact, PersonneContactAdmin)