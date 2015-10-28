# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitedemesure',
            name='formule',
            field=models.TextField(default=datetime.datetime(2015, 10, 25, 3, 53, 7, 364312, tzinfo=utc), blank='True', verbose_name='Formule'),
            preserve_default=False,
        ),
    ]
