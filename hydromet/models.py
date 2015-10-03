from django.db import models
from base.models import SiteSentinelle, PersonneContact


# Create your models here.

#  -------------------------------------------
#  Models for Hm
#  -------------------------------------------

class TypeStationPluviometrique(models.Model):
    typeStation = models.CharField(max_length=45, primary_key=True, verbose_name="Type de Station")
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")

    def __str__(self):              # __unicode__ on Python 2
        return self.typeStation


class StationPluviometrique(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    idSiteSeninnelle = models.ForeignKey(SiteSentinelle, verbose_name="Site Sentinelle", null=True, blank=True)
    nomStation = models.CharField(max_length=45, verbose_name="Nom de la Station")
    typeStation = models.ForeignKey(TypeStationPluviometrique, verbose_name="Type de la Station", null=True, blank=True)
    idStation = models.CharField(max_length=5, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nomStation


class ObservationTemperature(models.Model):
    temperatureMax = models.DecimalField(max_digits=5, decimal_places=3)
    temperatureMin = models.DecimalField(max_digits=5, decimal_places=3)
    idStation = models.ForeignKey(StationPluviometrique)
    valider = models.IntegerField()

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.temperatureMax


class ObservationPluviometrique(models.Model):
    quantite = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Quantite de Pluie")
    dateDebut = models.DateField(verbose_name="Date de debut")
    dateFin = models.DateField(verbose_name="Date de fin")
    description = models.TextField(max_length=100, blank=True)
    idStation = models.ForeignKey(StationPluviometrique, verbose_name="Nom de la Station")
    numeroJour = models.IntegerField(verbose_name="Numero du Jour")
    valider = models.BooleanField(verbose_name="Validation")

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
