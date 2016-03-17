from smslapli.regex import regex_percent
from django.contrib.gis.db import models
from base.models import Personne, Limite, UniteMesure
from django.contrib.auth.models import Group
from geoposition.fields import GeopositionField


#  -------------------------------------------
#  Models for Hm
#  -------------------------------------------


class TypeStation(models.Model):
    marque = models.CharField(max_length=100, blank=True)
    modele = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    automatique = models.BooleanField(default=False, help_text="Cochez si ce modèle est un modèle automatique.")

    class Meta:
        verbose_name = "Type de Station"
        verbose_name_plural = "Types de Station"

    def __str__(self):  # __unicode__ on Python 2
        return "%s, %s" % (self.marque, self.modele)


class Station(models.Model):
    limite = models.ForeignKey(Limite, null=True, blank=True, verbose_name="Zone")
    #latitude = models.FloatField(blank=True, null=True)
    #longitude = models.FloatField(blank=True, null=True)
    coordonnees_x_y = GeopositionField(null=True, blank=True, verbose_name="Position")
    #position = models.PointField(null=True, blank=True)
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
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


class ObservateurHydromet(models.Model):
    station = models.ForeignKey(Station)
    personne = models.OneToOneField(Personne)
    actif = models.BooleanField(default=True)

    class Meta:
        unique_together = ('station', 'personne')
        verbose_name = "Observateur (Pluviométrique)"
        verbose_name_plural = "Observateurs (Pluviométrique)"

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

    class Meta:
        verbose_name = "Type d'Observation (Pluviométrique)"
        verbose_name_plural = "Types d'Observation"

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
    observateurhydromet = models.ForeignKey(ObservateurHydromet, null=True, blank=True)
    limite = models.ForeignKey(Limite, null=True, blank=True)
    typeobservation = models.ForeignKey(TypeObservation, verbose_name="Type de l'Observation", null=True, blank=True)
    time_start = models.DateTimeField(verbose_name="Heure de Début", null=True, blank=True)
    time_end = models.DateTimeField(verbose_name="Heure de Fin", null=True, blank=True)
    time_result = models.DateTimeField(verbose_name="Date")
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Valeur de l'Observation")
    remarque = models.TextField(max_length=100, blank=True)
    valider = models.BooleanField(default=False)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s" % (self.time_result, self.value)


class Log(models.Model):
    observation = models.ForeignKey(Observation, null=True, default=None)
    observateurhydromet = models.ForeignKey(Personne, null=True, blank=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    time_result = models.DateTimeField()
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Valeur de l'Observation")

    @property
    def contact(self):
        if self.observateurhydromet:
            return "%s, %s" % (self.observateurhydromet.telephone_bureau, self.observateurhydromet.email)
        else:
            return "N/A"

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Log"

    def __str__(self):  # __unicode__ on Python 2
        return "%s, par %s " % (self.observation, self.observateurhydromet.nom if self.observateurhydromet else "N/A" )


class Alerte(models.Model):
    SUM = 'sum'
    AVG = 'avg'
    COUNT = 'count'
    MAX = 'max'
    MIN = 'min'
    TYPE_AGG = (
        (SUM, 'Somme'),
        (AVG, 'Moyenne'),
        (COUNT, 'Décompte'),
        (MAX, 'Maximum'),
        (MIN, 'Minimum'),
    )

    EQUAL = 'equal'
    SUP = 'sup'
    SUB = 'sub'
    TYPE_COMP = (
        (EQUAL, 'Egal'),
        (SUP, 'Suppérieur'),
        (SUB, 'Inférieur'),
    )

    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'

    UNITE_DUREE = (
        (HOUR, 'Heure'),
        (DAY, 'Jour'),
        (WEEK, 'Semaine'),
        (MONTH, 'Mois'),
        (YEAR, 'Année'),
    )
    nom = models.CharField(max_length=45, blank=True)
    description = models.TextField(max_length=100, blank=True)
    station = models.ForeignKey(Station, null=True, blank=True)
    typeobservation = models.ForeignKey(TypeObservation, verbose_name="Type de l'Observation", null=True, blank=True)
    type_aggregation = models.CharField(max_length=5, choices=TYPE_AGG, null=True, blank=True, default=SUM)
    type_comparaison = models.CharField(max_length=5, choices=TYPE_COMP, null=True, blank=True, default=EQUAL)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Valeur")
    duree = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    unite_duree = models.CharField(max_length=5, choices=UNITE_DUREE, null=True, blank=True, default=DAY)
    show_to_dashboard = models.BooleanField(default=True, verbose_name="Afficher sur le tableau de bord")
    send_by_email = models.BooleanField(default=False, verbose_name="Envoyer par Email")
    send_by_sms = models.BooleanField(default=False, verbose_name="Envoyer par SMS")
    groupe = models.ForeignKey(Group, verbose_name="Groupe Concerné", null=True, blank=True)
    note = models.TextField(max_length=100, blank=True)
    actif = models.BooleanField(default=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s" % (self.time_result, self.value)
