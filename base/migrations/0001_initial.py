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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('commune', models.CharField(verbose_name='Commune', max_length=45, unique=True)),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(verbose_name='Code', max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('departement', models.CharField(verbose_name='Departement', max_length=40, choices=[('Ouest', 'OUEST'), ('Nord', 'NORD'), ('Nordouest', 'NORD-OUEST'), ('Nordest', 'NORD-EST'), ('Sud', 'SUD'), ('Sudest', 'SUD-EST'), ('Artibonite', 'ARTIBONITE'), ('Nippes', 'NIPPES'), ('Centre', 'CENTRE'), ('Grandanse', "GRAND'ANSE")])),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(verbose_name='Code', max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nomPersonne', models.CharField(verbose_name='Nom', max_length=45)),
                ('prenomPersonne', models.CharField(verbose_name='Prenom', max_length=45)),
                ('telephoneBureau', models.CharField(blank=True, max_length=45, verbose_name='Telephone (Bureau)')),
                ('telephonePersonnel', models.CharField(verbose_name='Telephone (Personnel)', max_length=45, unique=True)),
                ('emailPersonnel', models.CharField(blank=True, max_length=45, verbose_name='Email (Personnel)')),
                ('adressePersonnelle', models.CharField(blank=True, max_length=45, verbose_name='Adresse (Personnlle)')),
                ('nif', models.CharField(verbose_name='NIF/CIN', max_length=45, unique=True)),
                ('dateEmbauche', models.DateField(verbose_name="Date d'embauche")),
                ('isactif', models.BooleanField(verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(primary_key=True, verbose_name='Poste', max_length=45, serialize=False, unique=True)),
                ('description', models.CharField(verbose_name='Description', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sectionCommunale', models.CharField(verbose_name='Section Communale', max_length=45)),
                ('nomOfficiel', models.CharField(blank=True, max_length=45, verbose_name='Nom officiel')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(verbose_name='Code', max_length=7, unique=True)),
                ('commune', models.ForeignKey(verbose_name='Commune', to='base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('localite', models.CharField(verbose_name='Localite', max_length=45)),
                ('latitude', models.DecimalField(max_digits=8, verbose_name='Latitude', default=0, decimal_places=2)),
                ('longitude', models.DecimalField(max_digits=8, verbose_name='Longitude', default=0, decimal_places=2)),
                ('hauteur', models.DecimalField(max_digits=8, verbose_name='Hauteur', default=0, decimal_places=2)),
                ('sectionCommunale', models.ForeignKey(verbose_name='Section Communale', to='base.SectionCommunale')),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(verbose_name='Poste', to='base.Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(verbose_name='Departement', to='base.Departement'),
        ),
    ]
