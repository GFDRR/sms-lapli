from django.db import models
from base.models import SiteSentinelle, PersonneContact

#  -------------------------------------------
#  Models for Hm
#  -------------------------------------------

class TypeStation(models.Model):
    typeStation = models.CharField(max_length=45, primary_key=True, verbose_name="Type de Station")
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")

    def __str__(self):              # __unicode__ on Python 2
        return self.typeStation

class UniteDeMesure(models.Model):
    uniteMesure = models.CharField(max_length=7, unique=True, verbose_name="Unite de mesure")
    description = models.TextField(blank=True)

    formule = models.TextField(verbose_name="Formule", blank="True")
    def __str__(self):              # __unicode__ on Python 2
         return self.uniteMesure

class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    idSiteSeninnelle = models.ForeignKey(SiteSentinelle, verbose_name="Site Sentinelle", null=True, blank=True)
    nomStation = models.CharField(max_length=45, verbose_name="Nom de la Station")
    typeStation = models.ForeignKey(TypeStation, verbose_name="Type de la Station", null=True, blank=True)
    idStation = models.CharField(max_length=5, blank=True)
    uniteMesure = models.ForeignKey(UniteDeMesure, verbose_name="Unite de mesure", null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nomStation

class StationObservers(models.Model):
    station = models.ForeignKey(Station)
    observer = models.OneToOneField(PersonneContact)

class Observation(models.Model):
    idStation = models.ForeignKey(Station)
    observer = models.ForeignKey(PersonneContact)
    timestamp = models.DateTimeField(auto_now_add=True)
    dateDebut = models.DateField(verbose_name="Debut")
    dateFin = models.DateField(verbose_name="Fin")
    temperatureMax = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Temperature max")
    temperatureMin = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Temperature min")
    quantitePluie = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Quantite de Pluie")
    description = models.TextField(max_length=100, blank=True)
    valider = models.BooleanField()
    valider = models.BooleanField(default=False)
<<<<<<< HEAD

    def __str__(self):              # __unicode__ on Python 2
        return self.idStation.nomStation + ' le '+ str(self.dateDebut)

    @property
    def log(self):
        return Log.objects.filter(observation=self.pk).count()

class Log(models.Model):
    observation = models.ForeignKey(Observation, null=True, blank=True, default = None)
    observer = models.ForeignKey(PersonneContact)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperatureMax = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Temperature max")
    temperatureMin = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Temperature min")
    quantitePluie = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Quantite de Pluie")

    def __str__(self):              # __unicode__ on Python 2
        return self.observer.nomPersonne + ' ' + self.observer.prenomPersonne
=======
>>>>>>> cf0fd66077cb8a4713fc0fcb7360cb8a4cbdfda0
