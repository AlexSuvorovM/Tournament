# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0003_fixture_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='matches_per_day',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fixture',
            name='rounds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fixture',
            name='start_date',
            field=models.DateTimeField(default=None, verbose_name='Start date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fixture',
            name='icon',
            field=models.ImageField(upload_to='static/icons', verbose_name='image'),
        ),
    ]
