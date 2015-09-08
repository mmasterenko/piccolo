# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assortiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('weight', models.PositiveSmallIntegerField()),
                ('weightUnits', models.CharField(max_length=3, choices=[('\u0433', '\u0433'), ('\u043a\u0433', '\u043a\u0433')])),
                ('pcs', models.DecimalField(max_digits=3, decimal_places=1)),
                ('days', models.PositiveSmallIntegerField()),
                ('isHit', models.BooleanField()),
                ('isNew', models.BooleanField()),
                ('isComingSoon', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='assortiment',
            name='category',
            field=models.ForeignKey(to='vapp.Category'),
        ),
    ]
