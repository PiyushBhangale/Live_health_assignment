# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180105_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprof',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprof',
            name='phone',
        ),
        migrations.AddField(
            model_name='userprof',
            name='note',
            field=models.TextField(default=b'0000000', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprof',
            name='title',
            field=models.TextField(default=b'0000000', max_length=100),
        ),
    ]
