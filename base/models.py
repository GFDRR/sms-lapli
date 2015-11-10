from smslapli.regex import regex_tel, regex_noid
from django.contrib.gis.db import models


# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------



class TypeLimite(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class Limite(models.Model):
    typelimite = models.ForeignKey(TypeLimite, verbose_name="Niveau")
    nom = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True)
    shape = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=20, blank=True)
    zone = models.PolygonField(null=True, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    objects = models.GeoManager()

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s " % (self.typelimite, self.nom)


class Poste(models.Model):
    nom_poste = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom_poste


class Personne(models.Model):
    poste = models.ForeignKey(Poste)
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    telephone_bureau = models.CharField(max_length=45, verbose_name="Telephone (Bureau)", validators=[
        regex_tel,
    ]
                                        )
    telephone_personnel = models.CharField(max_length=45, verbose_name="Telephone (Personnel)", blank=True,
                                           validators=[regex_tel, ])
    email = models.CharField(max_length=45, blank=True)
    adresse = models.TextField(max_length=100, blank=True)
    no_id = models.CharField(max_length=45, unique=True, verbose_name="NIF/CIN", validators=[
        regex_noid
    ]
                             )
    date_embauche = models.DateField(verbose_name="Date d'embauche")
    note = models.TextField(max_length=200, blank=True)
    actif = models.BooleanField()

    def __str__(self):  # __unicode__ on Python 2
        return "%s %s" % (self.nom, self.prenom)
