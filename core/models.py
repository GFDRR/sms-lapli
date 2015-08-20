from django.db import models

# Create your models here.
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
    latitude = models.CharField(max_length=45, blank=True)
    longitude = models.CharField(max_length=45, blank=True)
    hauteur = models.CharField(max_length=45, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.localite
