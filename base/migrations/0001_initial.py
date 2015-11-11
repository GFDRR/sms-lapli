# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Limite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('code', models.CharField(max_length=20, blank=True)),
                ('shape', django.contrib.gis.db.models.fields.PolygonField(null=True, blank=True, srid=4326)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('telephone_bureau', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond pas au format d'un numero de telephone", regex='^509[0-9]{8}$')], verbose_name='Telephone (Bureau)')),
                ('telephone_personnel', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond pas au format d'un numero de telephone", regex='^509[0-9]{8}$')], blank=True, verbose_name='Telephone (Personnel)')),
                ('email', models.CharField(max_length=45, blank=True)),
                ('adresse', models.TextField(max_length=100, blank=True)),
                ('no_id', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond ni au formt d'un code CIN ni a celui d'un NIF", regex='^[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{1}$|^\\d{2}-\\d{2}-\\d{2}-\\d{4}-\\d{2}-\\d{5}$')], verbose_name='NIF/CIN', unique=True)),
                ('date_embauche', models.DateField(verbose_name="Date d'embauche")),
                ('note', models.TextField(max_length=200, blank=True)),
                ('actif', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nom_poste', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeLimite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='personne',
            name='poste',
            field=models.ForeignKey(to='base.Poste'),
        ),
        migrations.AddField(
            model_name='limite',
            name='typelimite',
            field=models.ForeignKey(verbose_name='Niveau', to='base.TypeLimite'),
        ),
    ]
