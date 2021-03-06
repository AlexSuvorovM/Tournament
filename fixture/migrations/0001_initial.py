# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
                ('icon', models.FileField(blank=True, upload_to='icons/%Y/%m/%d/')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField(blank=True, null=True)),
                ('match_round', models.IntegerField()),
                ('status', models.CharField(choices=[('BYE', 'BYE'), ('Not Scheduled', 'Not Scheduled'), ('Scheduled', 'Scheduled'), ('Finished', 'Finished')], default='Not Scheduled', max_length=20)),
                ('winner', models.CharField(blank=True, choices=[('Player 1', 'Player 1'), ('Player 2', 'Player 2')], max_length=20)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='fixture.Fixture')),
                ('left_previous', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_next_match', to='fixture.Match')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='fixture.Fixture')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_matches', to='fixture.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_matches', to='fixture.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='right_previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_next_match', to='fixture.Match'),
        ),
        migrations.AddField(
            model_name='match',
            name='winning_palyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to='fixture.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('rank', 'fixture')]),
        ),
    ]
