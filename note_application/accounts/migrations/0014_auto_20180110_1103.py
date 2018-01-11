# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_noteclass_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteclass',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username'),
        ),
    ]
