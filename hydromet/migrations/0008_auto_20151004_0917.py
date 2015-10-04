# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_personnecontact_cfatachstation'),
        ('hydromet', '0007_auto_20151004_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('dateDebut', models.DateField(verbose_name=b'Date de debut')),
                ('dateFin', models.DateField(verbose_name=b'Date de fin')),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3)),
                ('quantitePluie', models.DecimalField(verbose_name=b'Quantite de Pluie', max_digits=15, decimal_places=2, blank=True)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('nomStation', models.CharField(max_length=45, verbose_name=b'Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(verbose_name=b'Site Sentinelle', blank=True, to='base.SiteSentinelle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.RenameModel(
            old_name='TypeStationPluviometrique',
            new_name='TypeStation',
        ),
        migrations.RemoveField(
            model_name='observationdirectionvent',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationhumidite',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationpluviometrique',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationtemperature',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='stationpluviometrique',
            name='idSiteSeninnelle',
        ),
        migrations.RemoveField(
            model_name='stationpluviometrique',
            name='typeStation',
        ),
        migrations.RemoveField(
            model_name='stationpluviometrique',
            name='uniteMesure',
        ),
        migrations.DeleteModel(
            name='ObservationDirectionVent',
        ),
        migrations.DeleteModel(
            name='ObservationHumidite',
        ),
        migrations.DeleteModel(
            name='ObservationPluviometrique',
        ),
        migrations.DeleteModel(
            name='ObservationTemperature',
        ),
        migrations.DeleteModel(
            name='StationPluviometrique',
        ),
        migrations.AddField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(verbose_name=b'Type de la Station', blank=True, to='hydromet.TypeStation', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(verbose_name=b'Unite de mesure', blank=True, to='hydromet.UniteDeMesure', null=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='idStation',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact', unique=True),
        ),
    ]
