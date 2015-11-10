# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0005_auto_20151107_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='note',
        ),
        migrations.RemoveField(
            model_name='log',
            name='observer',
        ),
        migrations.AddField(
            model_name='log',
            name='observateur',
            field=models.ForeignKey(null=True, to='hydromet.Observateur', blank=True),
        ),
    ]
