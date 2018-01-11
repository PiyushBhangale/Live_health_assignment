# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_noteclass_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteclass',
            name='user',
        ),
    ]
