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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature max', blank=True, null=True)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature min', blank=True, null=True)),
                ('quantitePluie', models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Quantite de Pluie', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name='Debut')),
                ('dateFin', models.DateField(verbose_name='Fin')),
                ('temperatureMax', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature max', blank=True, null=True)),
                ('temperatureMin', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Temperature min', blank=True, null=True)),
                ('quantitePluie', models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Quantite de Pluie', blank=True)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(max_digits=8, default=0, decimal_places=2)),
                ('nomStation', models.CharField(max_length=45, verbose_name='Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(to='base.SiteSentinelle', verbose_name='Site Sentinelle', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(max_length=45, serialize=False, primary_key=True, verbose_name='Type de Station')),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('uniteMesure', models.CharField(max_length=7, verbose_name='Unite de mesure', unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Formule', blank=True, null=True)),
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
            field=models.ForeignKey(to='hydromet.UniteDeMesure', verbose_name='Unite de mesure', blank=True, null=True),
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
            field=models.ForeignKey(to='hydromet.Observation', default=None, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
