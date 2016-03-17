from django.contrib.gis.db import models
from base.models import Personne, Limite



# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------
class TypeMarche(models.Model):
    type_marche = models.CharField(max_length=45, verbose_name="Type Marche")
    description = models.TextField(max_length=150, verbose_name="Description")

    def __str__(self):
        return self.type_marche


class Marche(models.Model):
    nom_marche = models.CharField(max_length=45, verbose_name="Marche")
    latitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Longitude")
    position = models.PointField(null=True, blank=True)
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Hauteur")
    typemarche = models.ForeignKey(TypeMarche, verbose_name="Type Marche")
    limite = models.ForeignKey(Limite, verbose_name="Section Communale", null=True)
    principale = models.BooleanField(verbose_name="Marché Principale", default=False)
    objects = models.GeoManager()

    def __str__(self):
        return self.nom_marche


class TypeProduit(models.Model):
    type_produit = models.CharField(max_length=45, verbose_name="Type Produit")
    description = models.TextField(max_length=150, verbose_name="Description")

    def __str__(self):
        return self.type_produit


class Produit(models.Model):
    code_produit = models.CharField(max_length=45, verbose_name="Code Produit")
    nom_produit = models.CharField(max_length=45, verbose_name="Nom Produit")
    marque = models.CharField(max_length=45, verbose_name="Marque")
    origine = models.CharField(max_length=45, verbose_name="Origine")
    typeproduit = models.ForeignKey(TypeProduit, verbose_name="Type Produit")

    def __str__(self):
        return self.nom_produit


class NiveauOffre(models.Model):
    niveau_offre = models.CharField(max_length=45, verbose_name="Niveau de l'offre")
    description = models.TextField(max_length=150, verbose_name="Description")

    def __str__(self):
        return self.niveau_offre


class ObservateurPrixMarche(models.Model):
    personne = models.ForeignKey(Personne, verbose_name="Observateur")
    actif = models.BooleanField(default=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s " % (self.personne, self.station)


class UniteMesure(models.Model):
    nom = models.CharField(max_length=45)
    unite = models.CharField(max_length=7, unique=True)
    description = models.TextField(blank=True)
    formule = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Formule")

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class ObservationDePrix(models.Model):
    date_collecte = models.DateTimeField(auto_now_add=True, verbose_name="Date collecte de donnees")
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix")
    marche = models.ForeignKey(Marche, verbose_name="Marche")
    produit = models.ForeignKey(Produit, verbose_name="Produit")
    unitemesure = models.ForeignKey(UniteMesure, verbose_name="Unite de mesure")
    niveauoffre = models.ForeignKey(NiveauOffre, verbose_name="Niveau de l'offre", null=True)
    observateurprixmarche = models.ForeignKey(ObservateurPrixMarche, null=True)
    description = models.TextField(max_length=100, blank=True)
    valider = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Observations de prix"

    @property
    def log(self):
        return Log.objects.filter(observation=self.pk).count()


class Log(models.Model):
    observation = models.ForeignKey(ObservationDePrix, null=True, blank=True, default=None)
    observateurprixmarche = models.ForeignKey(Personne, verbose_name="Observateur des prix du marché", related_name='collecteur')
    date_collecte = models.DateTimeField(auto_now_add=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix")
    marche = models.ForeignKey(Marche, verbose_name="Marche")
    produit = models.ForeignKey(Produit, verbose_name="Produit")
    unitemesure = models.ForeignKey(UniteMesure, verbose_name="Unite de mesure")
    niveauoffre = models.ForeignKey(NiveauOffre, verbose_name="Niveau de l'offre")

    def __str__(self):  # __unicode__ on Python 2
        return self.collecteur.nom + ' ' + self.collecteur.prenom
