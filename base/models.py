from smslapli.regex import regex_tel, regex_noid
from django.contrib.gis.db import models


# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------



class TypeLimite(models.Model):
    nom = models.CharField(max_length=40)
    niveau = models.IntegerField(default=0)
    description = models.TextField(max_length=100, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class Limite(models.Model):
    RURAL = 'rural'
    URBAIN = 'urbain'
    TYPE_LIMITE = (
        (RURAL, 'Rural'),
        (URBAIN, 'Urbain'),
    )
    typelimite = models.ForeignKey(TypeLimite, verbose_name="Niveau")
    nom = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True)
    code = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_LIMITE, null=True, blank=True)
    shape = models.PolygonField(null=True, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = "Limite Administrative"
        verbose_name_plural = "Limites Administratives"

    @property
    def departement(self):
        limite_lst = Limite.objects.get(typelimite__niveau=1, code=self.code[:2])
        if limite_lst :
            dept = limite_lst.nom
        else :
            dept = 'N/A'
        return dept

    @property
    def commune(self):
        limite_lst = Limite.objects.get(typelimite__niveau=3, code=self.code[:4])
        if limite_lst :
            commune = limite_lst.nom
        else :
            commune = 'N/A'
        return commune

    @property
    def section_communale(self):
        limite_lst = Limite.objects.get(typelimite__niveau=4, code=self.code[:7])
        if limite_lst :
            section_comm = limite_lst.nom
        else :
            section_comm = 'N/A'
        return section_comm

    def __str__(self):  # __unicode__ on Python 2
        return "%s : %s " % (self.typelimite, self.nom)


class Observatoire(models.Model):
    limite = models.ForeignKey(Limite, verbose_name="Département", limit_choices_to={'typelimite__niveau': '1'})
    nom = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=100, blank=True)
    actif = models.BooleanField(default=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.nom)


class ObservatoireLimite(models.Model):
    observatoire = models.ForeignKey(Observatoire)
    limite = models.ForeignKey(Limite)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('observatoire', 'limite')
        verbose_name = "Limite"
        verbose_name_plural = "Limites couvert par l'Observatoire"

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.observatoire)


class Poste(models.Model):
    nom_poste = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom_poste


class Personne(models.Model):
    poste = models.ForeignKey(Poste)
    observatoire = models.ForeignKey(Observatoire, blank=True, null=True)
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


class UniteMesure(models.Model):
    nom = models.CharField(max_length=45)
    unite = models.CharField(max_length=7, unique=True)
    description = models.TextField(blank=True)
    formule = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="Formule")

    class Meta:
        verbose_name = "Unité de Mesure"
        verbose_name_plural = "Unités de Mesure"

    def __str__(self):  # __unicode__ on Python 2
        return self.nom
