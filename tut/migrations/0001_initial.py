# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start_mileage', models.PositiveIntegerField(default=0)),
                ('start_time', models.DateTimeField(null=True)),
                ('stop_mileage', models.PositiveIntegerField(default=0)),
                ('stop_time', models.DateTimeField(null=True)),
                ('reporter', models.CharField(max_length=20)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
