# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0007_auto_20171123_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='winning_palyer',
        ),
        migrations.AddField(
            model_name='match',
            name='player_1_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='player_2_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to='fixture.Player'),
        ),
    ]
