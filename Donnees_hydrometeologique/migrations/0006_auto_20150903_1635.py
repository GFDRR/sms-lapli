# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0008_sitesentinelle'),
        ('Donnees_hydrometeologique', '0005_auto_20150903_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationDirectionVent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationHumidite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationPluviometrique',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantite', models.DecimalField(max_digits=15, default=0, decimal_places=2)),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('description', models.TextField(blank=True, max_length=100)),
                ('numeroJour', models.IntegerField()),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationTemperature',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationPluviometrique',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('latitude', models.DecimalField(max_digits=8, default=0, decimal_places=2)),
                ('longitude', models.DecimalField(max_digits=8, default=0, decimal_places=2)),
                ('hauteur', models.DecimalField(max_digits=8, default=0, decimal_places=2)),
                ('nomStation', models.CharField(max_length=45)),
                ('idSiteSeninnelle', models.ForeignKey(to='Donnees_de_base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationPluviometrique',
            fields=[
                ('typeStation', models.CharField(serialize=False, max_length=45, primary_key=True)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='stationpluviometrique',
            name='typeStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.TypeStationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationtemperature',
            name='idStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.StationPluviometrique'),
        ),
        migrations.AddField(
            model_name='observationpluviometrique',
            name='idStation',
            field=models.ForeignKey(to='Donnees_hydrometeologique.StationPluviometrique'),
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
