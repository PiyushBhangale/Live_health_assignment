# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20180110_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteclass',
            name='shared',
            field=models.BooleanField(default=False),
        ),
    ]
