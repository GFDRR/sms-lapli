# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0008_sitesentinelle'),
        ('Donnees_hydrometeologique', '0003_auto_20150903_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationDirectionVent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationHumidite',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationPluviometrique',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=15, default=0)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('temperatureMax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('temperatureMin', models.DecimalField(decimal_places=3, max_digits=5)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationPluviometrique',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
                ('hauteur', models.CharField(max_length=45)),
                ('nomStation', models.CharField(max_length=45)),
                ('idSiteSeninnelle', models.ForeignKey(to='Donnees_de_base.SiteSentinelle')),
                ('typeStation', models.ForeignKey(to='Donnees_hydrometeologique.TypeStationPluviometrique')),
            ],
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
