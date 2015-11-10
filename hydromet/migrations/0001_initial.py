# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('time_result', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, verbose_name="Valeur de l'Observation", blank=True, max_digits=15)),
                ('note', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('time_result', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, verbose_name="Valeur de l'Observation", blank=True, max_digits=15)),
                ('note', models.TextField(blank=True, max_length=100)),
                ('valider', models.BooleanField(default=False)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('limite', models.ForeignKey(to='base.Limite')),
                ('observer', models.ForeignKey(to='base.Personne')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('hauteur', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('nom', models.CharField(verbose_name='Nom de la Station', max_length=45)),
                ('code', models.CharField(null=True, blank=True, max_length=45, help_text='Le code est optionnel.', verbose_name='Code de la Station')),
                ('description', models.TextField(blank=True, max_length=100)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('limite', models.ForeignKey(null=True, blank=True, to='base.Limite')),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('observer', models.OneToOneField(to='base.Personne')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('max_value', models.DecimalField(decimal_places=2, null=True, max_digits=15, blank=True, verbose_name='Valeur Maximale Acceptée')),
                ('min_value', models.DecimalField(decimal_places=2, null=True, max_digits=15, blank=True, verbose_name='Valeur Minimale Acceptée')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('marque', models.CharField(blank=True, max_length=100)),
                ('modele', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(verbose_name='Description', blank=True, max_length=100)),
                ('automatique', models.BooleanField(default=False, help_text='Cochez si ce modèle est un modèle automatique.')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationTypeObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sos_standard', models.BooleanField(default=False, help_text='Cochez si le capteur répond au standard SOS.')),
                ('qualite', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(message='Saisissez un nombre entre 0 et 100', regex='^[1-9][0-9]?$|^100$|^0$')], blank=True)),
                ('typeobservation', models.ForeignKey(to='hydromet.TypeObservation')),
                ('typestation', models.ForeignKey(to='hydromet.TypeStation')),
            ],
        ),
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('unite', models.CharField(max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(decimal_places=3, null=True, max_digits=5, blank=True, verbose_name='Formule')),
            ],
        ),
        migrations.AddField(
            model_name='typestationtypeobservation',
            name='unitemesure',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Unite de mesure pour cette station', to='hydromet.UniteMesure'),
        ),
        migrations.AddField(
            model_name='typeobservation',
            name='unitemesure',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Unite de mesure par défaut', to='hydromet.UniteMesure'),
        ),
        migrations.AddField(
            model_name='station',
            name='typestation',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Type de la Station', to='hydromet.TypeStation'),
        ),
        migrations.AddField(
            model_name='observation',
            name='station',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='typeobservation',
            field=models.ForeignKey(verbose_name="Type de l'Observation", to='hydromet.TypeObservation'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(null=True, default=None, to='hydromet.Observation'),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.Personne'),
        ),
        migrations.AlterUniqueTogether(
            name='typestationtypeobservation',
            unique_together=set([('typestation', 'typeobservation')]),
        ),
        migrations.AlterUniqueTogether(
            name='stationobservers',
            unique_together=set([('station', 'observer')]),
        ),
    ]
