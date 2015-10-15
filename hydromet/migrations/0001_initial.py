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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature max', blank=True, null=True)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature min', blank=True, null=True)),
                ('quantitePluie', models.DecimalField(decimal_places=2, verbose_name='Quantite de Pluie', blank=True, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name='Debut')),
                ('dateFin', models.DateField(verbose_name='Fin')),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature max', blank=True, null=True)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature min', blank=True, null=True)),
                ('quantitePluie', models.DecimalField(decimal_places=2, verbose_name='Quantite de Pluie', blank=True, max_digits=15)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('nomStation', models.CharField(max_length=45, verbose_name='Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(blank=True, null=True, verbose_name='Site Sentinelle', to='base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(serialize=False, primary_key=True, max_length=45, verbose_name='Type de Station')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('uniteMesure', models.CharField(unique=True, max_length=7, verbose_name='Unite de mesure')),
                ('description', models.TextField(blank=True)),
                ('formule', models.TextField(verbose_name='Formule', blank='True')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Type de la Station', to='hydromet.TypeStation'),
        ),
        migrations.AddField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Unite de mesure', to='hydromet.UniteDeMesure'),
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
            field=models.ForeignKey(null=True, blank=True, default=None, to='hydromet.Observation'),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
