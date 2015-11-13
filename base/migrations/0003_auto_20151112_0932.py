# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_limite_niveau'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='limite',
            name='niveau',
        ),
        migrations.AddField(
            model_name='typelimite',
            name='niveau',
            field=models.IntegerField(default=0),
        ),
    ]
