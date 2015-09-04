# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0010_auto_20150904_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('commune', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('departement', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nomPersonne', models.CharField(max_length=45)),
                ('prenomPersonne', models.CharField(max_length=45)),
                ('telephoneBureau', models.CharField(blank=True, max_length=45)),
                ('telephonePersonnel', models.CharField(max_length=45)),
                ('emailPersonnel', models.CharField(max_length=45)),
                ('adressePersonnelle', models.CharField(max_length=45)),
                ('nif', models.CharField(blank=True, max_length=45)),
                ('cin', models.CharField(blank=True, max_length=45)),
                ('dateEmbauche', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(serialize=False, primary_key=True, max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('sectionCommunale', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('commune', models.ForeignKey(to='Donnees_de_base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('localite', models.CharField(max_length=45)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('hauteur', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
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
    ]
