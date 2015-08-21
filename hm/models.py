from django.db import models



# Create your models here.
from core.models import SiteSentinelle

class TypeStationPluviometrique(models.Model):
    typeStation = models.CharField(max_length=45, primary_key=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.description

class StationPluviometrique(models.Model):
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    hauteur = models.CharField(max_length=45)
    idSiteSeninnelle = models.ForeignKey(SiteSentinelle)
    nomStation = models.CharField(max_length=45)
    typeStation = models.ForeignKey(TypeStationPluviometrique)

    def __str__(self):              # __unicode__ on Python 2
        return self.latitude


class ObservationTemperature(models.Model):
    temperatureMax = models.DecimalField(max_digits=5, decimal_places=3)
    temperatureMin = models.DecimalField(max_digits=5, decimal_places=3)
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.temperatureMax

class ObservationPluviometrique(models.Model):
    quantite = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    description = models.TextField(max_length=100, blank=True)
    idStation = models.ForeignKey(StationPluviometrique)
    numeroJour = models.IntegerField()
    valider = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.description

class ObservationDirectionVent(models.Model):
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.valider

class ObservationHumidite(models.Model):
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.valider























