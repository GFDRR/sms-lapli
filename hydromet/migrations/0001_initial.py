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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(decimal_places=3, verbose_name='Temperature max', null=True, max_digits=5, blank=True)),
                ('temperatureMin', models.DecimalField(decimal_places=3, verbose_name='Temperature min', null=True, max_digits=5, blank=True)),
                ('quantitePluie', models.DecimalField(decimal_places=2, verbose_name='Quantite de Pluie', max_digits=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name='Debut')),
                ('dateFin', models.DateField(verbose_name='Fin')),
                ('temperatureMax', models.DecimalField(decimal_places=3, verbose_name='Temperature max', null=True, max_digits=5, blank=True)),
                ('temperatureMin', models.DecimalField(decimal_places=3, verbose_name='Temperature min', null=True, max_digits=5, blank=True)),
                ('quantitePluie', models.DecimalField(decimal_places=2, verbose_name='Quantite de Pluie', max_digits=15, blank=True)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('nomStation', models.CharField(max_length=45, verbose_name='Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(blank=True, to='base.SiteSentinelle', verbose_name='Site Sentinelle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(max_length=45, verbose_name='Type de Station', serialize=False, primary_key=True)),
                ('description', models.TextField(max_length=100, verbose_name='Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('uniteMesure', models.CharField(verbose_name='Unite de mesure', max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(decimal_places=3, verbose_name='Formule', null=True, max_digits=5, blank=True)),
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
            field=models.ForeignKey(blank=True, to='hydromet.Observation', default=None, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
