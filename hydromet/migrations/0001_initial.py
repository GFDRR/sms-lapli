# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('time_result', models.DateTimeField()),
                ('value', models.DecimalField(verbose_name="Valeur de l'Observation", blank=True, decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Observateur',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('actif', models.BooleanField(default=True)),
                ('personne', models.OneToOneField(to='base.Personne')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_start', models.DateTimeField(verbose_name='Heure de Début')),
                ('time_end', models.DateTimeField(verbose_name='Heure de Fin')),
                ('time_result', models.DateTimeField(verbose_name='Date')),
                ('value', models.DecimalField(verbose_name="Valeur de l'Observation", blank=True, decimal_places=2, max_digits=15)),
                ('note', models.TextField(blank=True, max_length=100)),
                ('valider', models.BooleanField(default=False)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('limite', models.ForeignKey(null=True, blank=True, to='base.Limite')),
                ('observateur', models.ForeignKey(null=True, blank=True, to='hydromet.Observateur')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(null=True, blank=True, srid=4326)),
                ('hauteur', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('nom', models.CharField(verbose_name='Nom de la Station', max_length=45)),
                ('code', models.CharField(null=True, blank=True, verbose_name='Code de la Station', max_length=45, help_text='Le code est optionnel.')),
                ('description', models.TextField(blank=True, max_length=100)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('limite', models.ForeignKey(null=True, blank=True, to='base.Limite', verbose_name='Zone')),
            ],
        ),
        migrations.CreateModel(
            name='TypeObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('max_value', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=15, verbose_name='Valeur Maximale Acceptée')),
                ('min_value', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=15, verbose_name='Valeur Minimale Acceptée')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('marque', models.CharField(blank=True, max_length=100)),
                ('modele', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(verbose_name='Description', blank=True, max_length=100)),
                ('automatique', models.BooleanField(default=False, help_text='Cochez si ce modèle est un modèle automatique.')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStationTypeObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sos_standard', models.BooleanField(default=False, help_text='Cochez si le capteur répond au standard SOS.')),
                ('qualite', models.IntegerField(null=True, blank=True, validators=[django.core.validators.RegexValidator(regex='^[1-9][0-9]?$|^100$|^0$', message='Saisissez un nombre entre 0 et 100')])),
                ('typeobservation', models.ForeignKey(to='hydromet.TypeObservation')),
                ('typestation', models.ForeignKey(to='hydromet.TypeStation')),
            ],
        ),
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('unite', models.CharField(unique=True, max_length=7)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=5, verbose_name='Formule')),
            ],
        ),
        migrations.AddField(
            model_name='typestationtypeobservation',
            name='unitemesure',
            field=models.ForeignKey(null=True, blank=True, to='hydromet.UniteMesure', verbose_name='Unite de mesure pour cette station'),
        ),
        migrations.AddField(
            model_name='typeobservation',
            name='unitemesure',
            field=models.ForeignKey(null=True, blank=True, to='hydromet.UniteMesure', verbose_name='Unite de mesure par défaut'),
        ),
        migrations.AddField(
            model_name='station',
            name='typestation',
            field=models.ForeignKey(null=True, blank=True, to='hydromet.TypeStation', verbose_name='Type de la Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='station',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='typeobservation',
            field=models.ForeignKey(null=True, blank=True, to='hydromet.TypeObservation', verbose_name="Type de l'Observation"),
        ),
        migrations.AddField(
            model_name='observateur',
            name='station',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='log',
            name='observateur',
            field=models.ForeignKey(null=True, blank=True, to='hydromet.Observateur'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(null=True, default=None, to='hydromet.Observation'),
        ),
        migrations.AlterUniqueTogether(
            name='typestationtypeobservation',
            unique_together=set([('typestation', 'typeobservation')]),
        ),
        migrations.AlterUniqueTogether(
            name='observateur',
            unique_together=set([('station', 'personne')]),
        ),
    ]
