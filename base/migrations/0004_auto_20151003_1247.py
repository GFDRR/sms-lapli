# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_departement_ihsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='id_code',
            field=models.TextField(unique=True, max_length=4, blank=True),
        ),
        migrations.AddField(
            model_name='departement',
            name='id_code',
            field=models.TextField(unique=True, max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='sectioncommunale',
            name='id_code',
            field=models.TextField(unique=True, max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='commune',
            name='commune',
            field=models.CharField(unique=True, max_length=45, verbose_name=b'Commune'),
        ),
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(unique=True, max_length=40, verbose_name=b'Departement'),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='adressePersonnelle',
            field=models.CharField(max_length=45, verbose_name=b'Adresse (Personnlle)', blank=True),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='emailPersonnel',
            field=models.CharField(max_length=45, verbose_name=b'Email (Personnel)', blank=True),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='telephonePersonnel',
            field=models.CharField(unique=True, max_length=45, verbose_name=b'Telephone (Personnel)'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='nomPoste',
            field=models.CharField(max_length=45, unique=True, serialize=False, verbose_name=b'Poste', primary_key=True),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='sectionCommunale',
            field=models.CharField(unique=True, max_length=45, verbose_name=b'Section Communale'),
        ),
    ]
