# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0008_auto_20171124_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='current_round',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Match Date'),
        ),
    ]
