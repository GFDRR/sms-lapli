from django.contrib import admin

# Register your models here.

from .models import *

class StationPluviometriqueAdmin(admin.ModelAdmin):
    list_display = ("id__SiteSeninnelle", "latitude", "longitude", "hauteur", "nomStation", "type__Station")

    def id__SiteSeninnelle(self, instance):
        return instance.idSiteSeninnelle.id

    def type__Station(self, instance):
        return instance.typeStation.typeStation


class ObservationPluviometriqueAdmin(admin.ModelAdmin):
    list_display = ("quantite", "dateDebut", "dateFin", "description", "id_Station", "valider")

    def id_Station(self, instance):
        return instance.idStation.id


class TypeStationPluviometriqueAdmin(admin.ModelAdmin):
    list_display = ("typeStation", "description")

# class ObservationTemperatureAdmin(admin.ModelAdmin):
#
#
# class ObservationDirectionVentAdmin(admin.ModelAdmin):
#
# class ObservationHumiditeAdmin(admin.ModelAdmin):


admin.site.register(StationPluviometrique, StationPluviometriqueAdmin)
admin.site.register(TypeStationPluviometrique, TypeStationPluviometriqueAdmin)
# admin.site.register(ObservationTemperature)
admin.site.register(ObservationPluviometrique, ObservationPluviometriqueAdmin)
# admin.site.register(ObservationDirectionVent)
# admin.site.register(ObservationHumidite)