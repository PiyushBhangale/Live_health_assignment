# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180106_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='note',
            field=models.TextField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprof',
            name='title',
            field=models.TextField(default=None, max_length=100),
        ),
    ]
