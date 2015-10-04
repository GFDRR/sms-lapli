# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151003_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnecontact',
            name='isactif',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commune',
            name='commune',
            field=models.CharField(max_length=45, verbose_name='Commune', unique=True),
        ),
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(max_length=40, verbose_name='Departement', unique=True),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='adressePersonnelle',
            field=models.CharField(max_length=45, blank=True, verbose_name='Adresse (Personnlle)'),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='emailPersonnel',
            field=models.CharField(max_length=45, blank=True, verbose_name='Email (Personnel)'),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='telephonePersonnel',
            field=models.CharField(max_length=45, verbose_name='Telephone (Personnel)', unique=True),
        ),
        migrations.AlterField(
            model_name='poste',
            name='nomPoste',
            field=models.CharField(serialize=False, max_length=45, unique=True, verbose_name='Poste', primary_key=True),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='sectionCommunale',
            field=models.CharField(max_length=45, verbose_name='Section Communale'),
        ),
    ]
