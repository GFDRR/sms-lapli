from django.contrib import admin

# Register your models here.

from .forms import *
from .models import *

class DepartementAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("departement", "id_code", "description")
    form = DepartementForm




class CommuneAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("departement", "commune", "id_code", "description")
    form = CommuneForm




class SectionCommunaleAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("commune", "sectionCommunale", "nomOfficiel", "id_code", "description")
    form = SectionCommunaleForm



class SiteSentinelleAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("sectionCommunale", "localite", "latitude", "longitude", "hauteur")
    form = SiteSentinelleForm



class PosteAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("nomPoste", "description")
    form = PosteForm


class PersonneContactAdmin(admin.ModelAdmin):
    list_display = ("nomPoste", "nomPersonne", "prenomPersonne", "telephoneBureau", "telephonePersonnel", "emailPersonnel", "adressePersonnelle", "nif", "dateEmbauche", "isactif")
    list_filter = (('isactif',))
    search_fields = ["nomPersonne", "prenomPersonne", "telephoneBureau", "telephonePersonnel", "emailPersonnel", "adressePersonnelle", "nif", "dateEmbauche"]
    form = PersonneContactForm

    #return the nomPoste of the foreignkey(s) in list_display and it will show it


#Added all in the register
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(SectionCommunale, SectionCommunaleAdmin)
admin.site.register(SiteSentinelle, SiteSentinelleAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(PersonneContact, PersonneContactAdmin)
