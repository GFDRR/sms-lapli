# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='description',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='description',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='hauteur',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='latitude',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='longitude',
            field=models.CharField(max_length=45, blank=True),
        ),
    ]
