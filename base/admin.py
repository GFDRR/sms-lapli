from django.contrib.gis import admin

# Register your models here.

from base.models import TypeLimite, Limite, Poste, Personne, Observatoire, ObservatoireLimite

class ObservatoireLimiteInline(admin.StackedInline):
    model = ObservatoireLimite
    extra = 1


class TypeLimiteAdmin(admin.ModelAdmin):
    list_display = ("nom", "niveau", "description")
    ordering = ['niveau']


class LimiteAdmin(admin.GeoModelAdmin):
    list_display = ("departement", "commune", "section_communale", "typelimite", "nom", "code", )
    list_filter = ('typelimite',)
    search_fields = ["nom", "code"]
    ordering = ['code', 'nom']


class PosteAdmin(admin.ModelAdmin):
    list_display = ("nom_poste", "description")


class PersonneAdmin(admin.ModelAdmin):
    list_display = (
        "nom", "prenom", "poste",  "telephone_bureau", "email",
        "date_embauche", "actif")
    list_filter = ('actif', "date_embauche",)
    search_fields = ["nom", "prenom", "telephone_bureau", "telephone_personnel", "email",
                     "adresse", "nif"]


class ObservatoireAdmin(admin.ModelAdmin):
    list_display = (
        "limite", "nom", "actif")
    list_filter = ('limite', 'actif',)
    search_fields = ["nom"]
    inlines = [ObservatoireLimiteInline]


# Added all in the register
admin.site.register(Observatoire, ObservatoireAdmin)
admin.site.register(Poste)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(TypeLimite, TypeLimiteAdmin)
admin.site.register(Limite, LimiteAdmin)


