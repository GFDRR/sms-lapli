from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(StationPluviometrique)
admin.site.register(TypeStationPluviometrique)
admin.site.register(ObservationTemperature)
admin.site.register(ObservationPluviometrique)
admin.site.register(ObservationDirectionVent)
admin.site.register(ObservationHumidite)