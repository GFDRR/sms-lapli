from django.db import models



# Create your models here.

#  -------------------------------------------
#  Models for Hm
#  -------------------------------------------

from Donnees_de_base.models import SiteSentinelle

class TypeStationPluviometrique(models.Model):
    typeStation = models.CharField(max_length=45, primary_key=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.typeStation

class StationPluviometrique(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    idSiteSeninnelle = models.ForeignKey(SiteSentinelle)
    nomStation = models.CharField(max_length=45)
    typeStation = models.ForeignKey(TypeStationPluviometrique)

    def __int__(self):              # __unicode__ on Python 2
        return self.id


class ObservationTemperature(models.Model):
    temperatureMax = models.DecimalField(max_digits=5, decimal_places=3)
    temperatureMin = models.DecimalField(max_digits=5, decimal_places=3)
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.temperatureMax

class ObservationPluviometrique(models.Model):
    quantite = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    description = models.TextField(max_length=100, blank=True)
    idStation = models.ForeignKey(StationPluviometrique)
    numeroJour = models.IntegerField()
    valider = models.IntegerField()

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.description

class ObservationDirectionVent(models.Model):
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.valider

class ObservationHumidite(models.Model):
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.valider
























