from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------


class Departement(models.Model):
    departement = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
         return self.departement


class Commune(models.Model):
    departement = models.ForeignKey(Departement)
    commune = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
         return self.commune


class SectionCommunale(models.Model):
    commune = models.ForeignKey(Commune)
    sectionCommunale = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
         return self.sectionCommunale


class SiteSentinelle(models.Model):
    sectionCommunale = models.ForeignKey(SectionCommunale)
    localite = models.CharField(max_length=45)
    latitude = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.localite


class Poste(models.Model):
    nomPoste = models.CharField(max_length=45, primary_key= True)
    description = models.CharField(max_length=45)

    def __str__(self):              # __unicode__ on Python 2
         return self.nomPoste


class PersonneContact(models.Model):
    nomPoste = models.ForeignKey(Poste)
    nomPersonne = models.CharField(max_length=45)
    prenomPersonne = models.CharField(max_length=45)
    telephoneBureau = models.CharField(max_length=45, blank=True)
    telephonePersonnel = models.CharField(max_length=45)
    emailPersonnel = models.CharField(max_length=45)
    adressePersonnelle = models.CharField(max_length=45)
    nif = models.CharField(max_length=45, blank=True)
    cin = models.CharField(max_length=45, blank=True)
    dateEmbauche = models.DateField()
    cfAtachStation = models.ForeignKey('Donnees_hydrometeologique.StationPluviometrique', verbose_name="Affectation Station")

    def __str__(self):              # __unicode__ on Python 2
         return self.telephonePersonnel

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

