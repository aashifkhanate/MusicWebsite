# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-26 22:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180208_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.FileField(default=datetime.datetime(2018, 7, 26, 22, 59, 32, 48735, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
