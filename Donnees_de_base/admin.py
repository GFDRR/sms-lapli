from django.contrib import admin

# Register your models here.

from .forms import *
from .models import *

class DepartementAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("departement", "description")
    form = DepartementForm




class CommuneAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("get_departement", "commune", "description")
    form = CommuneForm

    #return the departement of the foreignkey(s) in list_display and it will show it
    def get_departement(self, instance):
        return instance.departement.departement



class SectionCommunaleAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("commune", "sectionCommunale", "description")
    form = SectionCommunaleForm



class SiteSentinelleAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("get_sectionCommunale", "localite", "latitude", "longitude", "hauteur")
    form = SiteSentinelleForm

    #return the sectionCommunale of the foreignkey(s) in list_display and it will show it
    def get_sectionCommunale(self, instance):
        return instance.sectionCommunale.sectionCommunale



class PosteAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("nomPoste", "description")
    form = PosteForm


class PersonneContactAdmin(admin.ModelAdmin):
    list_display = ("get_nomPoste", "nomPersonne", "prenomPersonne", "telephoneBureau", "telephonePersonnel", "emailPersonnel", "adressePersonnelle", "nif", "cin", "dateEmbauche")
    form = PersonneContactForm

    #return the nomPoste of the foreignkey(s) in list_display and it will show it
    def get_nomPoste(self, instance):
        return instance.nomPoste.nomPoste

#Added all in the register
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(SectionCommunale, SectionCommunaleAdmin)
admin.site.register(SiteSentinelle, SiteSentinelleAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(PersonneContact, PersonneContactAdmin)