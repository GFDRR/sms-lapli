# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0004_auto_20150820_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffectationSiteSentinelle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('PersonneContact_idPersonneContact', models.IntegerField()),
                ('SiteSentinelle_idSiteSentinelle', models.IntegerField()),
                ('dateAffectation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nomPersonne', models.CharField(max_length=45)),
                ('prenomPersonne', models.CharField(max_length=45)),
                ('telephoneBureau', models.CharField(max_length=45)),
                ('telephonePersonnel', models.CharField(max_length=45)),
                ('emailPersonnel', models.CharField(max_length=45)),
                ('adressePersonnelle', models.CharField(max_length=45)),
                ('nif', models.CharField(blank=True, max_length=45)),
                ('cin', models.CharField(blank=True, max_length=45)),
                ('dateEmbauche', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(to='Donnees_de_base.Poste'),
        ),
        migrations.AlterUniqueTogether(
            name='affectationsitesentinelle',
            unique_together=set([('PersonneContact_idPersonneContact', 'SiteSentinelle_idSiteSentinelle')]),
        ),
    ]
