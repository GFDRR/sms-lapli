from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *


class StationPluviometriqueAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_display = ("idSiteSeninnelle", "latitude", "longitude", "hauteur", "nomStation", "typeStation")
    form = StationPluviometriqueForm


class ObservationPluviometriqueAdmin(admin.ModelAdmin):

    #Called my form in the admin and set a column for each fields
    list_display = ("quantite", "dateDebut", "dateFin", "description", "Nom_station", "valider")
    form = ObservationPluviometriqueForm

    #return id of the foreignkey(s) in list_display and it will show it
    def Nom_station(self, instance):
        return instance.idStation.nomStation


class TypeStationPluviometriqueAdmin(admin.ModelAdmin):
    #Called my form in the admin and set a column for each fields
    list_display = ("typeStation", "description")
    form = TypeStationPluviometriqueForm

# class ObservationTemperatureAdmin(admin.ModelAdmin):
#
#
# class ObservationDirectionVentAdmin(admin.ModelAdmin):
#
# class ObservationHumiditeAdmin(admin.ModelAdmin):


#Added all in the register
admin.site.register(StationPluviometrique, StationPluviometriqueAdmin)
admin.site.register(TypeStationPluviometrique, TypeStationPluviometriqueAdmin)
admin.site.register(ObservationPluviometrique, ObservationPluviometriqueAdmin)

# admin.site.register(ObservationTemperature)
# admin.site.register(ObservationDirectionVent)
# admin.site.register(ObservationHumidite)