# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name='Debut')),
                ('dateFin', models.DateField(verbose_name='Fin')),
                ('temperatureMax', models.DecimalField(decimal_places=3, max_digits=5, null=True, blank=True, verbose_name='Temperature max')),
                ('temperatureMin', models.DecimalField(decimal_places=3, max_digits=5, null=True, blank=True, verbose_name='Temperature min')),
                ('quantitePluie', models.DecimalField(decimal_places=2, max_digits=15, blank=True, verbose_name='Quantite de Pluie')),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('nomStation', models.CharField(max_length=45, verbose_name='Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(to='base.SiteSentinelle', blank=True, verbose_name='Site Sentinelle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(serialize=False, primary_key=True, max_length=45, verbose_name='Type de Station')),
                ('description', models.TextField(max_length=100, blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('uniteMesure', models.CharField(unique=True, max_length=7, verbose_name='Unite de mesure')),
                ('description', models.TextField(blank=True)),
                ('formule', models.TextField(blank='True', verbose_name='Formule')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(to='hydromet.TypeStation', blank=True, verbose_name='Type de la Station', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(to='hydromet.UniteDeMesure', blank=True, verbose_name='Unite de mesure', null=True),
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
    ]
