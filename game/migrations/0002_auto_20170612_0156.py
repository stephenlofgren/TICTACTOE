# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='active_player_num',
            field=models.SmallIntegerField(choices=[(0, 'player1'), (1, 'player2')], default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='state_sequence',
            field=models.CharField(default='---------', max_length=9),
        ),
    ]
