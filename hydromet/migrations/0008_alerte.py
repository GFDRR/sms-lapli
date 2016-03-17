# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0007_auto_20160316_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerte',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type_aggregation', models.CharField(default='sum', choices=[('sum', 'Somme'), ('avg', 'Moyenne'), ('count', 'Décompte'), ('max', 'Maximum'), ('min', 'Minimum')], null=True, blank=True, max_length=5)),
                ('type_comparaison', models.CharField(default='equal', choices=[('equal', 'Egal'), ('sup', 'Suppérieur'), ('sub', 'Inférieur')], null=True, blank=True, max_length=5)),
                ('value', models.DecimalField(max_digits=15, blank=True, verbose_name='Valeur', decimal_places=2)),
                ('duree', models.PositiveSmallIntegerField(null=True, blank=True, default=1)),
                ('unite_duree', models.CharField(default='day', choices=[('hour', 'Heure'), ('day', 'Jour'), ('week', 'Semaine'), ('month', 'Mois'), ('year', 'Année')], null=True, blank=True, max_length=5)),
                ('show_to_dashboard', models.BooleanField(default=True, verbose_name='Afficher sur le tableau de bord')),
                ('send_by_email', models.BooleanField(default=False, verbose_name='Envoyer par Email')),
                ('send_by_sms', models.BooleanField(default=False, verbose_name='Envoyer par SMS')),
                ('note', models.TextField(blank=True, max_length=100)),
                ('actif', models.BooleanField(default=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('station', models.ForeignKey(to='hydromet.Station', null=True, blank=True)),
                ('typeobservation', models.ForeignKey(verbose_name="Type de l'Observation", to='hydromet.TypeObservation', null=True, blank=True)),
            ],
        ),
    ]
