# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151112_0932'),
        ('hydromet', '0002_station_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_collecte', models.DateTimeField(auto_now_add=True)),
                ('prix', models.DecimalField(default=0, decimal_places=2, verbose_name='Prix', max_digits=8)),
                ('collecteur', models.ForeignKey(related_name='collecteur', verbose_name='Collecteur', to='base.Personne')),
            ],
        ),
        migrations.CreateModel(
            name='Marche',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom_marche', models.CharField(max_length=45, verbose_name='Marche')),
                ('latitude', models.DecimalField(default=0, decimal_places=2, verbose_name='Latitude', max_digits=8)),
                ('longitude', models.DecimalField(default=0, decimal_places=2, verbose_name='Longitude', max_digits=8)),
                ('hauteur', models.DecimalField(default=0, decimal_places=2, verbose_name='Hauteur', max_digits=8)),
                ('limite', models.ForeignKey(null=True, verbose_name='Section Communale', to='base.Limite')),
            ],
        ),
        migrations.CreateModel(
            name='NiveauOffre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('niveau_offre', models.CharField(max_length=45, verbose_name="Niveau de l'offre")),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ObservationDePrix',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_collecte', models.DateTimeField(auto_now_add=True, verbose_name='Date collecte de donnees')),
                ('prix', models.DecimalField(default=0, decimal_places=2, verbose_name='Prix', max_digits=8)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('valider', models.BooleanField(default=False)),
                ('marche', models.ForeignKey(verbose_name='Marche', to='prix_marche.Marche')),
                ('observateur', models.ForeignKey(null=True, to='base.Personne')),
            ],
            options={
                'verbose_name_plural': 'Observations de prix',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code_produit', models.CharField(max_length=45, verbose_name='Code Produit')),
                ('nom_produit', models.CharField(max_length=45, verbose_name='Nom Produit')),
                ('marque', models.CharField(max_length=45, verbose_name='Marque')),
                ('origine', models.CharField(max_length=45, verbose_name='Origine')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMarche',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type_marche', models.CharField(max_length=45, verbose_name='Type Marche')),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type_produit', models.CharField(max_length=45, verbose_name='Type Produit')),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='typeproduit',
            field=models.ForeignKey(verbose_name='Type Produit', to='prix_marche.TypeProduit'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='produit',
            field=models.ForeignKey(verbose_name='Produit', to='prix_marche.Produit'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='unitemesure',
            field=models.ForeignKey(verbose_name='Unite de mesure', to='hydromet.UniteMesure'),
        ),
        migrations.AddField(
            model_name='marche',
            name='typemarche',
            field=models.ForeignKey(verbose_name='Type Marche', to='prix_marche.TypeMarche'),
        ),
        migrations.AddField(
            model_name='log',
            name='marche',
            field=models.ForeignKey(verbose_name='Marche', to='prix_marche.Marche'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(null=True, to='prix_marche.ObservationDePrix', default=None, blank=True),
        ),
        migrations.AddField(
            model_name='log',
            name='produit',
            field=models.ForeignKey(verbose_name='Produit', to='prix_marche.Produit'),
        ),
        migrations.AddField(
            model_name='log',
            name='unitemesure',
            field=models.ForeignKey(verbose_name='Unite de mesure', to='hydromet.UniteMesure'),
        ),
    ]
