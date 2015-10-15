# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=3, verbose_name='Temperature max')),
                ('temperatureMin', models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=3, verbose_name='Temperature min')),
                ('quantitePluie', models.DecimalField(max_digits=15, blank=True, decimal_places=2, verbose_name='Quantite de Pluie')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name='Debut')),
                ('dateFin', models.DateField(verbose_name='Fin')),
                ('temperatureMax', models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=3, verbose_name='Temperature max')),
                ('temperatureMin', models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=3, verbose_name='Temperature min')),
                ('quantitePluie', models.DecimalField(max_digits=15, blank=True, decimal_places=2, verbose_name='Quantite de Pluie')),
                ('description', models.TextField(blank=True, max_length=100)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(max_digits=8, decimal_places=2, default=0)),
                ('nomStation', models.CharField(verbose_name='Nom de la Station', max_length=45)),
                ('idStation', models.CharField(blank=True, max_length=5)),
                ('idSiteSeninnelle', models.ForeignKey(blank=True, to='base.SiteSentinelle', verbose_name='Site Sentinelle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(primary_key=True, verbose_name='Type de Station', max_length=45, serialize=False)),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('uniteMesure', models.CharField(verbose_name='Unite de mesure', max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.TextField(blank='True', verbose_name='Formule')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(blank=True, to='hydromet.TypeStation', verbose_name='Type de la Station', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(blank=True, to='hydromet.UniteDeMesure', verbose_name='Unite de mesure', null=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='idStation',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(blank=True, to='hydromet.Observation', null=True, default=None),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
