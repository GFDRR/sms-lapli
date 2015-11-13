from django.contrib import admin

# Register your models here.

#from .forms import *
from .models import TypeLimite, Limite, Poste, Personne


class TypeLimiteAdmin(admin.ModelAdmin):
    # Called my form in the admin and set a column for each fields
    list_display = ("nom", "niveau", "description")
    ordering = ['niveau']
    # form = PosteForm


class LimiteAdmin(admin.ModelAdmin):
    # Called my form in the admin and set a column for each fields
    list_display = ("typelimite", "nom", "code")
    list_filter = ('typelimite',)
    search_fields = ["nom", "code"]
    # form = PosteForm


class PosteAdmin(admin.ModelAdmin):
    # Called my form in the admin and set a column for each fields
    list_display = ("nom_poste", "description")
    # form = PosteForm


class PersonneAdmin(admin.ModelAdmin):
    list_display = (
        "nom", "prenom", "poste",  "telephone_bureau", "email",
        "date_embauche", "actif")
    list_filter = ('actif', "date_embauche",)
    search_fields = ["nom", "prenom", "telephone_bureau", "telephone_personnel", "email",
                     "adresse", "nif"]
    #form = PersonneContactForm


# Added all in the register
admin.site.register(Poste)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(TypeLimite, TypeLimiteAdmin)
admin.site.register(Limite, LimiteAdmin)


