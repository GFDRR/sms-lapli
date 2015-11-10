# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import *


# def validate(modeladmin, request, queryset):
#     queryset.update(valider=1)
# validate.short_description = "Valider les observations selectionnées"
#
# def unvalidate(modeladmin, request, queryset):
#     queryset.update(valider=0)
# unvalidate.short_description = "Invalider les observations selectionnées"
#

# class StationAdmin(admin.ModelAdmin):
#
#     #Called my form in the admin and set a column for each fields
#     list_display = ("id","idSiteSeninnelle", "idStation", "latitude", "longitude", "hauteur", "uniteMesure", "nomStation", "typeStation")
#     search_fields = ["latitude", "longitude", "hauteur", "nomStation"]
#
#
#
# class ObservationAdmin(admin.ModelAdmin):
#
#     #Called my form in the admin and set a column for each fields
#
#     list_display = ("quantitePluie", "dateDebut", "dateFin", "description", "valider")
#     list_filter = (('valider',))
#     search_fields = ["quantitePluie", "dateDebut", "dateFin", "description", "timestamp"]
#
#     list_display = ("idStation", "observer", "quantitePluie", "timestamp", "dateDebut", "dateFin", "description", "valider")
#
#     list_filter = (('valider',))
#     search_fields = ["quantitePluie", "dateDebut", "dateFin", "description", "timestamp"]
#
#     list_display = ("idStation", "observer", "timestamp", "dateDebut", "dateFin", "temperatureMax", "temperatureMin", "quantitePluie", "description", "valider")
#
#
#     list_display = ('pk',"idStation", "observer", "timestamp", "dateDebut", "dateFin", "temperatureMax", "temperatureMin", "quantitePluie", "description", "valider")
#
#     list_display = ('pk',"idStation", "observer", "timestamp", "dateDebut", "dateFin",  "quantitePluie", "log", "description", "valider")
#
#     list_display = ('pk',"idStation", "observer", "timestamp", "dateDebut", "dateFin", "temperatureMax", "temperatureMin", "quantitePluie", "description", "valider")
#
#     form = ObservationForm
#     # actions = [validate, unvalidate]
#     actions = ['make_valider', 'make_nonvalider']
#     def get_actions(self, request):
#         actions = super(ObservationAdmin, self).get_actions(request)
#         if not request.user.is_superuser:
#             if  'make_valider' in actions:
#                 del actions['make_valider']
#             if 'make_nonvalider' in actions:
#                 del actions['make_nonvalider']
#         return actions
#
#
#
#     #return id of the foreignkey(s) in list_display and it will show it
#     def Nom_station(self, instance):
#         return instance.idStation.nomStation
#
#     def make_valider(self, request, queryset):
#         # rows_updated = queryset.update(status='v')
#         rows_updated = queryset.update(valider=True)
#         if rows_updated == 1:
#             message_bit = "1 Observation pluviometrique was"
#
#         else:
#             message_bit = "%s Observation pluviometrique  were" % rows_updated
#         self.message_user(request, "%s successfully marked as inValid." % message_bit)
#
#     make_valider.short_description = "Valider les observations selectionnées"
#
#     def make_nonvalider(self, request, queryset):
#         # rows_updated = queryset.update(status='v')
#         rows_updated = queryset.update(valider=False)
#         if rows_updated == 1:
#             message_bit = "1 Observation pluviometrique was"
#
#         else:
#             message_bit = "%s Observation pluviometrique  were" % rows_updated
#         self.message_user(request, "%s successfully marked as Invalid." % message_bit)
#
#     make_nonvalider.short_description = "Invalider les observations selectionnées"



# class TypeStationAdmin(admin.ModelAdmin):
#     #Called my form in the admin and set a column for each fields
#     list_display = ("typeStation", "description")
#     search_fields = ["typeStation"]
#
# class UniteDeMesureAdmin(admin.ModelAdmin):
#     list_display = ("uniteMesure", "formule", "description")
#
# class StationObserversAdmin(admin.ModelAdmin):
#     list_display = ("station", "observer")
#     search_fields = ["station"]
#
# class LogAdmin(admin.ModelAdmin):
#     list_display = ("observation", "observer", "quantitePluie", "timestamp")
#     search_fields = ["timestamp"]


class TypeStationTypeObservationInline(admin.StackedInline):
    model = TypeStationTypeObservation
    extra = 3


class TypeStationAdmin(admin.ModelAdmin):
    inlines = [TypeStationTypeObservationInline]

class StationAdmin(admin.ModelAdmin):
    list_display = ("nom", "typestation" ,"limite")

class ObservateurAdmin(admin.ModelAdmin):
    list_display = ("station", "personne")

class ObservationAdmin(admin.ModelAdmin):
    list_display = ("station", "typeobservation", "value", "time_result", "log", "valider")
    list_filter = ('limite',)
    search_fields = ["nom"]

class LogAdmin(admin.ModelAdmin):
    list_display = ("observation", "observateur", "contact", "time_result", "value")
    list_filter = ('time_result', 'observation')
    #search_fields = ["nom"]


# Added all in the register
admin.site.register(Station, StationAdmin)
admin.site.register(TypeStation, TypeStationAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(UniteMesure)
admin.site.register(Observateur, ObservateurAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(TypeObservation)
#admin.site.register(TypeStationTypeObservation)
