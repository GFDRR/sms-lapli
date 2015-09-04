# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffectationSiteSentinelle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('PersonneContact_idPersonneContact', models.IntegerField()),
                ('SiteSentinelle_idSiteSentinelle', models.IntegerField()),
                ('dateAffectation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('commune', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('departement', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nomPersonne', models.CharField(max_length=45)),
                ('prenomPersonne', models.CharField(max_length=45)),
                ('telephoneBureau', models.CharField(max_length=45)),
                ('telephonePersonnel', models.CharField(max_length=45)),
                ('emailPersonnel', models.CharField(max_length=45)),
                ('adressePersonnelle', models.CharField(max_length=45)),
                ('nif', models.CharField(max_length=45, blank=True)),
                ('cin', models.CharField(max_length=45, blank=True)),
                ('dateEmbauche', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sectionCommunale', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('commune', models.ForeignKey(to='Donnees_de_base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('localite', models.CharField(max_length=45)),
                ('latitude', models.CharField(max_length=45, blank=True)),
                ('longitude', models.CharField(max_length=45, blank=True)),
                ('hauteur', models.CharField(max_length=45, blank=True)),
                ('sectionCommunale', models.ForeignKey(to='Donnees_de_base.SectionCommunale')),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(to='Donnees_de_base.Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(to='Donnees_de_base.Departement'),
        ),
        migrations.AlterUniqueTogether(
            name='affectationsitesentinelle',
            unique_together=set([('PersonneContact_idPersonneContact', 'SiteSentinelle_idSiteSentinelle')]),
        ),
    ]
