# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0004_auto_20171123_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='start_date',
            field=models.DateField(verbose_name='Start date'),
        ),
    ]
