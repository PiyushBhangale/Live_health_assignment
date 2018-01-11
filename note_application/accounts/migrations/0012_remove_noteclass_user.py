# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180110_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteclass',
            name='user',
        ),
    ]
