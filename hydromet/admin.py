# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from hydromet.models import TypeStationTypeObservation, TypeStation, Observateur, Observation, TypeObservation, Station, UniteMesure, Log

def validate(modeladmin, request, queryset):
    queryset.update(valider=True)
validate.short_description = "Valider les observations selectionnées"

def unvalidate(modeladmin, request, queryset):
    queryset.update(valider=False)
unvalidate.short_description = "Invalider les observations selectionnées"


class TypeStationTypeObservationInline(admin.StackedInline):
    model = TypeStationTypeObservation
    extra = 3


class TypeStationAdmin(admin.ModelAdmin):
    inlines = [TypeStationTypeObservationInline]

class StationAdmin(admin.ModelAdmin):
    list_display = ("nom", "typestation" ,"limite")
    search_fields = ["nom"]

class ObservateurAdmin(admin.ModelAdmin):
    list_display = ("station", "personne")

class ObservationAdmin(admin.ModelAdmin):
    list_display = ("station", "typeobservation", "value", "time_result", "log", "valider")
    list_filter = ('limite', 'time_result',)
    search_fields = ["station__nom", "time_result"]
    actions = [validate, unvalidate]
    ordering = ['-time_result', 'station']
    date_hierarchy = 'time_result'

class LogAdmin(admin.ModelAdmin):
    list_display = ("observation", "observateur", "contact", "time_result", "value")
    list_filter = ('time_result', 'observation')
    #search_fields = ["nom"]

class TypeObservationAdmin(admin.ModelAdmin):
    list_display = ("nom", "unitemesure")
    search_fields = ["nom"]


# Added all in the register
admin.site.register(Station, StationAdmin)
admin.site.register(TypeStation, TypeStationAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(UniteMesure)
admin.site.register(Observateur, ObservateurAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(TypeObservation, TypeObservationAdmin)