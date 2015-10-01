# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationDirectionVent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationHumidite',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationPluviometrique',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantite', models.DecimalField(decimal_places=2, verbose_name='Quantite de Pluie', max_digits=15, blank=True)),
                ('dateDebut', models.DateField(verbose_name='Date de debut')),
                ('dateFin', models.DateField(verbose_name='Date de fin')),
                ('description', models.TextField(max_length=100, blank=True)),
                ('numeroJour', models.IntegerField(verbose_name='Numero du Jour')),
                ('valider', models.IntegerField(verbose_name='Validation')),
            ],
        ),
        migrations.CreateModel(
            name='ObservationTemperature',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationPluviometrique',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('hauteur', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('nomStation', models.CharField(max_length=45, verbose_name='Nom de la Station')),
                ('idSiteSeninnelle', models.ForeignKey(verbose_name='Site Sentinelle', to='Donnees_de_base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationPluviometrique',
            fields=[
                ('typeStation', models.CharField(max_length=45, primary_key=True, verbose_name='Type de Station', serialize=False)),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='stationpluviometrique',
            name='typeStation',
            field=models.ForeignKey(verbose_name='Type de la Station', to='Donnees_hydrometeologique.TypeStationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationtemperature',
            name='idStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.StationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationpluviometrique',
            name='idStation',
            field=models.ForeignKey(verbose_name='Nom de la Station', to='Donnees_hydrometeologique.StationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationhumidite',
            name='idStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.StationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationdirectionvent',
            name='idStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.StationPluviometrique'),
        ),
    ]
