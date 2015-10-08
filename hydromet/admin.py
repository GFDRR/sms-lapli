from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *


def validate(modeladmin, request, queryset):
    queryset.update(valider=1)
validate.short_description = "Valider les observations selectionnées"

def unvalidate(modeladmin, request, queryset):
    queryset.update(valider=0)
unvalidate.short_description = "Invalider les observations selectionnées"


class StationAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_display = ("id","idSiteSeninnelle", "idStation", "latitude", "longitude", "hauteur", "uniteMesure", "nomStation", "typeStation")
    search_fields = ["latitude", "longitude", "hauteur", "nomStation"]
    form = StationForm


class ObservationAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_filter = (('valider',))
    search_fields = ["quantitePluie", "dateDebut", "dateFin", "description"]
    list_display = ('pk',"idStation", "observer", "timestamp", "dateDebut", "dateFin", "temperatureMax", "temperatureMin", "quantitePluie", "description", "valider")
    form = ObservationForm
    actions = [validate, unvalidate]

    #return id of the foreignkey(s) in list_display and it will show it
    def Nom_station(self, instance):
        return instance.idStation.nomStation


class TypeStationAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("typeStation", "description")
    search_fields = ["typeStation"]
    form = TypeStationForm

class UniteDeMesureAdmin(admin.ModelAdmin):
    list_display = ("uniteMesure", "formule", "description")
    form = UniteDeMesureForm

class StationObserversAdmin(admin.ModelAdmin):
    list_display = ("station", "observer")
    search_fields = ["station"]
    form = StationObserversForm

# class ObservationTemperatureAdmin(admin.ModelAdmin):
#
#
# class ObservationDirectionVentAdmin(admin.ModelAdmin):
#
# class ObservationHumiditeAdmin(admin.ModelAdmin):


#Added all in the register
admin.site.register(Station, StationAdmin)
admin.site.register(TypeStation, TypeStationAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(UniteDeMesure, UniteDeMesureAdmin)
admin.site.register(StationObservers, StationObserversAdmin)

# admin.site.register(ObservationTemperature)
# admin.site.register(ObservationDirectionVent)
# admin.site.register(ObservationHumidite)
