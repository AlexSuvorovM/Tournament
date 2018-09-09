# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0005_auto_20171123_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateField(default=None, verbose_name='Match Date'),
            preserve_default=False,
        ),
    ]
