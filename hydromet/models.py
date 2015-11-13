from smslapli.regex import regex_percent
#from django.db import models
from django.contrib.gis.db import models
from base.models import Personne, Limite


#  -------------------------------------------
#  Models for Hm
#  -------------------------------------------


class TypeStation(models.Model):
    marque = models.CharField(max_length=100, blank=True)
    modele = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    automatique = models.BooleanField(default=False, help_text="Cochez si ce modèle est un modèle automatique.")

    def __str__(self):  # __unicode__ on Python 2
        return "%s, %s" % (self.marque, self.modele)


class UniteMesure(models.Model):
    nom = models.CharField(max_length=45)
    unite = models.CharField(max_length=7, unique=True)
    description = models.TextField(blank=True)
    formule = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Formule")

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class Station(models.Model):
    limite = models.ForeignKey(Limite, null=True, blank=True, verbose_name="Zone")
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    position = models.PointField(null=True, blank=True)
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    nom = models.CharField(max_length=45, verbose_name="Nom de la Station")
    code = models.CharField(max_length=45, verbose_name="Code de la Station", null=True, blank=True,
                            help_text="Le code est optionnel.")
    typestation = models.ForeignKey(TypeStation, verbose_name="Type de la Station", null=True, blank=True)
    description = models.TextField(max_length=100, blank=True)
    actif = models.BooleanField(default=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    objects = models.GeoManager()

    @property
    def typelimite(self):
        return self.limite.typelimite

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class Observateur(models.Model):
    station = models.ForeignKey(Station)
    personne = models.OneToOneField(Personne)
    actif = models.BooleanField(default=True)

    class Meta:
        unique_together = ('station', 'personne')

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s " % (self.personne, self.station)


class TypeObservation(models.Model):
    nom = models.CharField(max_length=45)
    unitemesure = models.ForeignKey(UniteMesure, verbose_name="Unite de mesure par défaut", null=True, blank=True)
    description = models.TextField(max_length=100, blank=True)
    max_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,
                                    verbose_name="Valeur Maximale Acceptée")
    min_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,
                                    verbose_name="Valeur Minimale Acceptée")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % self.nom


class TypeStationTypeObservation(models.Model):
    typestation = models.ForeignKey(TypeStation)
    typeobservation = models.ForeignKey(TypeObservation)
    unitemesure = models.ForeignKey(UniteMesure, verbose_name="Unite de mesure pour cette station", null=True, blank=True)
    sos_standard = models.BooleanField(default=False, help_text="Cochez si le capteur répond au standard SOS.")
    qualite = models.IntegerField(blank=True, null=True, validators=[
        regex_percent,
    ])

    class Meta:
        unique_together = ('typestation', 'typeobservation',)

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % self.unitemesure


class Observation(models.Model):
    station = models.ForeignKey(Station)
    observateur = models.ForeignKey(Observateur, null=True, blank=True)
    limite = models.ForeignKey(Limite, null=True, blank=True)
    typeobservation = models.ForeignKey(TypeObservation, verbose_name="Type de l'Observation", null=True, blank=True)
    time_start = models.DateTimeField(verbose_name="Heure de Début")
    time_end = models.DateTimeField(verbose_name="Heure de Fin")
    time_result = models.DateTimeField(verbose_name="Date")
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Valeur de l'Observation")
    note = models.TextField(max_length=100, blank=True)
    valider = models.BooleanField(default=False)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    @property
    def log(self):
        return Log.objects.filter(observation=self.pk).count()


    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s" % (self.time_result, self.value)


class Log(models.Model):
    observation = models.ForeignKey(Observation, null=True, default=None)
    observateur = models.ForeignKey(Observateur, null=True, blank=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    time_result = models.DateTimeField()
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Valeur de l'Observation")

    @property
    def contact(self):
        return "%s, %s" % (self.observateur.personne.telephone_bureau, self.observateur.personne.email)

    def __str__(self):  # __unicode__ on Python 2
        return "%s, par %s " % (self.observation, self.observateur.personne.nom)
        #return "%s" % self.time_result
