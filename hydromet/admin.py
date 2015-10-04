from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *


class StationAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_display = ("idSiteSeninnelle", "latitude", "longitude", "hauteur", "nomStation", "typeStation")
    form = StationForm


class ObservationAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_display = ("idStation", "observer", "quantitePluie", "timestamp", "dateDebut", "dateFin", "description", "valider")
    form = ObservationForm

    #return id of the foreignkey(s) in list_display and it will show it
    def Nom_station(self, instance):
        return instance.idStation.nomStation


class TypeStationAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("typeStation", "description")
    form = TypeStationForm

class UniteDeMesureAdmin(admin.ModelAdmin):
    list_display = ("uniteMesure", "description")
    form = UniteDeMesureForm

class StationObserversAdmin(admin.ModelAdmin):
    list_display = ("station", "observer")
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
