# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20180110_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharednotes',
            name='note_id',
        ),
        migrations.RemoveField(
            model_name='sharednotes',
            name='shared_by',
        ),
        migrations.RemoveField(
            model_name='sharednotes',
            name='shared_to',
        ),
        migrations.AddField(
            model_name='noteclass',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Sharednotes',
        ),
    ]
