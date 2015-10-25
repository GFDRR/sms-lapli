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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('commune', models.CharField(max_length=45, verbose_name='Commune', unique=True)),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
                ('id_code', models.CharField(max_length=7, verbose_name='Code', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('departement', models.CharField(max_length=40, verbose_name='Departement')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
                ('id_code', models.CharField(max_length=7, verbose_name='Code', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nomPersonne', models.CharField(max_length=45, verbose_name='Nom')),
                ('prenomPersonne', models.CharField(max_length=45, verbose_name='Prenom')),
                ('telephoneBureau', models.CharField(max_length=45, verbose_name='Telephone (Bureau)', blank=True)),
                ('telephonePersonnel', models.CharField(max_length=45, verbose_name='Telephone (Personnel)', unique=True)),
                ('emailPersonnel', models.CharField(max_length=45, verbose_name='Email (Personnel)', blank=True)),
                ('adressePersonnelle', models.CharField(max_length=45, verbose_name='Adresse (Personnlle)', blank=True)),
                ('nif', models.CharField(max_length=45, verbose_name='NIF/CIN', unique=True)),
                ('dateEmbauche', models.DateField(verbose_name="Date d'embauche")),
                ('isactif', models.BooleanField(verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(max_length=45, primary_key=True, unique=True, verbose_name='Poste', serialize=False)),
                ('description', models.CharField(max_length=45, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sectionCommunale', models.CharField(max_length=45, verbose_name='Section Communale')),
                ('nomOfficiel', models.CharField(max_length=45, verbose_name='Nom officiel', blank=True)),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
                ('id_code', models.CharField(max_length=7, verbose_name='Code', unique=True)),
                ('commune', models.ForeignKey(to='base.Commune', verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('localite', models.CharField(max_length=45, verbose_name='Localite')),
                ('latitude', models.DecimalField(decimal_places=2, verbose_name='Latitude', default=0, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=2, verbose_name='Longitude', default=0, max_digits=8)),
                ('hauteur', models.DecimalField(decimal_places=2, verbose_name='Hauteur', default=0, max_digits=8)),
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
