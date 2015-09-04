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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationHumidite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationPluviometrique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantite', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('description', models.TextField(max_length=100, blank=True)),
                ('numeroJour', models.IntegerField()),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationTemperature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('temperatureMax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('temperatureMin', models.DecimalField(decimal_places=3, max_digits=5)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationPluviometrique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
                ('hauteur', models.CharField(max_length=45)),
                ('nomStation', models.CharField(max_length=45)),
                ('cfPersCnt', models.ForeignKey(to='Donnees_de_base.PersonneContact')),
                ('idSiteSeninnelle', models.ForeignKey(to='Donnees_de_base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationPluviometrique',
            fields=[
                ('typeStation', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=100, blank=True)),
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
