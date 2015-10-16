# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('commune', models.CharField(unique=True, max_length=45, verbose_name='Commune')),
                ('description', models.TextField(max_length=100, blank=True, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('departement', models.CharField(max_length=40, choices=[('Ouest', 'OUEST'), ('Nord', 'NORD'), ('Nordouest', 'NORD-OUEST'), ('Nordest', 'NORD-EST'), ('Sud', 'SUD'), ('Sudest', 'SUD-EST'), ('Artibonite', 'ARTIBONITE'), ('Nippes', 'NIPPES'), ('Centre', 'CENTRE'), ('Grandanse', "GRAND'ANSE")], verbose_name='Departement')),
                ('description', models.TextField(max_length=100, blank=True, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nomPersonne', models.CharField(max_length=45, verbose_name='Nom')),
                ('prenomPersonne', models.CharField(max_length=45, verbose_name='Prenom')),
                ('telephoneBureau', models.CharField(max_length=45, blank=True, verbose_name='Telephone (Bureau)')),
                ('telephonePersonnel', models.CharField(unique=True, max_length=45, verbose_name='Telephone (Personnel)')),
                ('emailPersonnel', models.CharField(max_length=45, blank=True, verbose_name='Email (Personnel)')),
                ('adressePersonnelle', models.CharField(max_length=45, blank=True, verbose_name='Adresse (Personnlle)')),
                ('nif', models.CharField(unique=True, max_length=45, verbose_name='NIF/CIN')),
                ('dateEmbauche', models.DateField(verbose_name="Date d'embauche")),
                ('isactif', models.BooleanField(verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(serialize=False, primary_key=True, unique=True, max_length=45, verbose_name='Poste')),
                ('description', models.CharField(max_length=45, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sectionCommunale', models.CharField(max_length=45, verbose_name='Section Communale')),
                ('nomOfficiel', models.CharField(max_length=45, blank=True, verbose_name='Nom officiel')),
                ('description', models.TextField(max_length=100, blank=True, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
                ('commune', models.ForeignKey(to='base.Commune', verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('localite', models.CharField(max_length=45, verbose_name='Localite')),
                ('latitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Longitude')),
                ('hauteur', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Hauteur')),
                ('sectionCommunale', models.ForeignKey(to='base.SectionCommunale', verbose_name='Section Communale')),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(to='base.Poste', verbose_name='Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(to='base.Departement', verbose_name='Departement'),
        ),
    ]
