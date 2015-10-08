from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------


class Departement(models.Model):
    departement = models.CharField(max_length=40, verbose_name="Departement")
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    id_code = models.CharField(max_length=7, unique=True, verbose_name="Code")
    # ihsi = models.CharField(max_length=10, verbose_name="Code IHSI")

    def __str__(self):              # __unicode__ on Python 2
         return self.departement


class Commune(models.Model):
    departement = models.ForeignKey(Departement, verbose_name="Departement")
    commune = models.CharField(max_length=45, verbose_name="Commune", unique=True)
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    id_code = models.CharField(max_length=7, unique=True, verbose_name="Code")

    def __str__(self):              # __unicode__ on Python 2
         return self.commune


class SectionCommunale(models.Model):
    commune = models.ForeignKey(Commune, verbose_name="Commune")
    sectionCommunale = models.CharField(max_length=45, verbose_name="Section Communale")
    nomOfficiel = models.CharField(max_length=45, blank=True, verbose_name="Nom officiel")
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    id_code = models.CharField(max_length=7, unique=True, verbose_name="Code")

    def __str__(self):              # __unicode__ on Python 2
         return self.sectionCommunale


class SiteSentinelle(models.Model):
    sectionCommunale = models.ForeignKey(SectionCommunale, verbose_name="Section Communale")
    localite = models.CharField(max_length=45, verbose_name="Localite")
    latitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Longitude")
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Hauteur")

    def __str__(self):              # __unicode__ on Python 2
        return self.localite


class Poste(models.Model):
    nomPoste = models.CharField(max_length=45, primary_key=True, verbose_name="Poste", unique=True)
    description = models.CharField(max_length=45, verbose_name="Description")

    def __str__(self):              # __unicode__ on Python 2
         return self.nomPoste


class PersonneContact(models.Model):
    nomPoste = models.ForeignKey(Poste, verbose_name="Poste")
    nomPersonne = models.CharField(max_length=45, verbose_name="Nom")
    prenomPersonne = models.CharField(max_length=45, verbose_name="Prenom")
    telephoneBureau = models.CharField(max_length=45, blank=True, verbose_name="Telephone (Bureau)")
    telephonePersonnel = models.CharField(max_length=45, verbose_name="Telephone (Personnel)", unique=True)
    emailPersonnel = models.CharField(max_length=45, verbose_name="Email (Personnel)", blank=True)
    adressePersonnelle = models.CharField(max_length=45, verbose_name="Adresse (Personnlle)", blank=True)
    nif = models.CharField(max_length=45, unique=True, verbose_name="NIF/CIN")
    dateEmbauche = models.DateField(verbose_name="Date d'embauche")
    isactif = models.BooleanField(verbose_name="Active")

    def __str__(self):              # __unicode__ on Python 2
         return "%s %s" % (self.nomPersonne, self.prenomPersonne)

# class AffectationSiteSentinelle(models.Model):
#     PersonneContact_idPersonneContact = models.IntegerField(blank=False,null=False)
#     SiteSentinelle_idSiteSentinelle = models.IntegerField(blank=False,null=False)
#     dateAffectation = models.DateField()
#
#     class Meta:
#         unique_together = ('PersonneContact_idPersonneContact', 'SiteSentinelle_idSiteSentinelle');
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.dateAffectation

# validators=[
#      RegexValidator(
#            regex= r'^[a-zA-Z\'-]+\s$', #r'^\[a-zA-Z]["\'|-]?\[a-zA-Z]$',
#            message= ('Username must be Alphanumeric'),
#        ),]
