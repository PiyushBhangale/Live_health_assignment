# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180106_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=None, max_length=100)),
                ('note', models.TextField(default=None, max_length=1000)),
            ],
        ),
    ]
