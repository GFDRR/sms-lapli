from django.db import models

# Create your models here.
class Departement(models.Model):
    departement = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True)



class Commune(models.Model):
    departement = models.ForeignKey(Departement)
    commune = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)



class SectionCommunale(models.Model):
    commune = models.ForeignKey(Commune)
    sectionCommunale = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)



class SiteSentinelle(models.Model):
    sectionCommunale = models.ForeignKey(SectionCommunale)
    localite = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45, blank=True)
    longitude = models.CharField(max_length=45, blank=True)
    hauteur = models.CharField(max_length=45, blank=True)




class Poste(models.Model):
    nomPoste = models.CharField(max_length=45, primary_key= True)
    description = models.CharField(max_length=45)





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



