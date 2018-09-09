# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0002_remove_fixture_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='icon',
            field=models.ImageField(default=None, upload_to='icons', verbose_name='image'),
            preserve_default=False,
        ),
    ]
