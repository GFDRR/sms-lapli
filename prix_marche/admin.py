from django.contrib import admin

# Register your models here.
from .models import *

def validate(modeladmin, request, queryset):
    queryset.update(valider=True)
validate.short_description = "Valider les observations selectionnées"


def unvalidate(modeladmin, request, queryset):
    queryset.update(valider=False)
unvalidate.short_description = "Invalider les observations selectionnées"

class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['nom_produit']

class ObservationDePrixAdmin(admin.ModelAdmin):
    list_display = ("date_collecte", "marche", "produit", "prix", "unitemesure", "observateurprixmarche", "valider")
    # list_filter = ['marche__sectionCommunale__commune__departement', 'marche__sectionCommunale__commune', 'marche__sectionCommunale' , 'marche', 'produit', 'valider']
    list_filter = ['marche', 'produit', 'valider']
    actions = [validate, unvalidate]

admin.site.register(TypeMarche)
admin.site.register(ObservateurPrixMarche)
admin.site.register(Marche)
admin.site.register(TypeProduit)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(ObservationDePrix, ObservationDePrixAdmin)
admin.site.register(NiveauOffre)