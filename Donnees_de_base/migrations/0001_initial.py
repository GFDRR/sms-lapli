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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('commune', models.CharField(max_length=45, verbose_name='Commune')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('departement', models.CharField(max_length=40, verbose_name='Departement')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
                ('ihsi', models.CharField(max_length=10, verbose_name='Code IHSI')),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nomPersonne', models.CharField(max_length=45, verbose_name='Nom')),
                ('prenomPersonne', models.CharField(max_length=45, verbose_name='Prenom')),
                ('telephoneBureau', models.CharField(max_length=45, verbose_name='Telephone (Bureau)', blank=True)),
                ('telephonePersonnel', models.CharField(max_length=45, verbose_name='Telephone (Personnel)')),
                ('emailPersonnel', models.CharField(max_length=45, verbose_name='Email (Personnel)')),
                ('adressePersonnelle', models.CharField(max_length=45, verbose_name='Adresse (Personnlle)')),
                ('nif', models.CharField(max_length=45, verbose_name='NIF/CIN', unique=True)),
                ('dateEmbauche', models.DateField(verbose_name="Date d'embauche")),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(max_length=45, primary_key=True, verbose_name='Poste', serialize=False)),
                ('description', models.CharField(max_length=45, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sectionCommunale', models.CharField(max_length=45, verbose_name='Section Communale')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
                ('commune', models.ForeignKey(verbose_name='Commune', to='Donnees_de_base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('localite', models.CharField(max_length=45, verbose_name='Localite')),
                ('latitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Longitude')),
                ('hauteur', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Hauteur')),
                ('sectionCommunale', models.ForeignKey(verbose_name='Section Communale', to='Donnees_de_base.SectionCommunale')),
            ],
        ),
    ]
