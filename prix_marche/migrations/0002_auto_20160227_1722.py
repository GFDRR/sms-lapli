# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151112_0932'),
        ('prix_marche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservateurPrixMarche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actif', models.BooleanField(default=True)),
                ('personne', models.ForeignKey(to='base.Personne', verbose_name='Observateur')),
            ],
        ),
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('unite', models.CharField(max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True, verbose_name='Formule')),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='collecteur',
        ),
        migrations.RemoveField(
            model_name='observationdeprix',
            name='observateur',
        ),
        migrations.AddField(
            model_name='log',
            name='niveauoffre',
            field=models.ForeignKey(to='prix_marche.NiveauOffre', verbose_name="Niveau de l'offre", null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='observateurprixmarche',
            field=models.ForeignKey(to='base.Personne', related_name='collecteur', verbose_name='Observateur des prix du marché', null=True),
        ),
        migrations.AddField(
            model_name='marche',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='marche',
            name='principale',
            field=models.BooleanField(default=False, verbose_name='Marché Principale'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='niveauoffre',
            field=models.ForeignKey(to='prix_marche.NiveauOffre', verbose_name="Niveau de l'offre", null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='unitemesure',
            field=models.ForeignKey(to='prix_marche.UniteMesure', verbose_name='Unite de mesure'),
        ),
        migrations.AlterField(
            model_name='observationdeprix',
            name='unitemesure',
            field=models.ForeignKey(to='prix_marche.UniteMesure', verbose_name='Unite de mesure'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='observateurprixmarche',
            field=models.ForeignKey(to='prix_marche.ObservateurPrixMarche', null=True),
        ),
    ]
