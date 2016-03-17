# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_unitemesure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observatoire',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nom', models.CharField(blank=True, max_length=40)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObservatoireLimite',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='limite',
            options={'verbose_name_plural': 'Limites Administratives', 'verbose_name': 'Limite Administrative'},
        ),
        migrations.AddField(
            model_name='limite',
            name='type',
            field=models.CharField(null=True, blank=True, max_length=2, choices=[('rural', 'Rural'), ('urbain', 'Urbain')]),
        ),
        migrations.AddField(
            model_name='observatoirelimite',
            name='limite',
            field=models.ForeignKey(to='base.Limite'),
        ),
        migrations.AddField(
            model_name='observatoirelimite',
            name='observatoire',
            field=models.ForeignKey(to='base.Observatoire'),
        ),
        migrations.AddField(
            model_name='observatoire',
            name='limite',
            field=models.ForeignKey(to='base.Limite', verbose_name='Département'),
        ),
        migrations.AddField(
            model_name='personne',
            name='observatoire',
            field=models.ForeignKey(null=True, to='base.Observatoire', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='observatoirelimite',
            unique_together=set([('observatoire', 'limite')]),
        ),
    ]
