# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0011_auto_20150904_1118'),
        ('Donnees_hydrometeologique', '0008_auto_20150904_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationDirectionVent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationHumidite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationPluviometrique',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantite', models.DecimalField(blank=True, max_digits=15, decimal_places=2)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('temperatureMax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('temperatureMin', models.DecimalField(decimal_places=3, max_digits=5)),
                ('valider', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationPluviometrique',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('hauteur', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('nomStation', models.CharField(max_length=45)),
                ('cfPersCnt', models.ForeignKey(to='Donnees_de_base.PersonneContact')),
                ('idSiteSeninnelle', models.ForeignKey(to='Donnees_de_base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationPluviometrique',
            fields=[
                ('typeStation', models.CharField(serialize=False, primary_key=True, max_length=45)),
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
