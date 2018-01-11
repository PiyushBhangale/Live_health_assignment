# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_noteclass_shared'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sharednotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameField(
            model_name='noteclass',
            old_name='shared',
            new_name='completed',
        ),
        migrations.AddField(
            model_name='sharednotes',
            name='note_id',
            field=models.ForeignKey(to='accounts.Noteclass'),
        ),
        migrations.AddField(
            model_name='sharednotes',
            name='shared_by',
            field=models.ForeignKey(related_name='shared_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharednotes',
            name='shared_to',
            field=models.ForeignKey(related_name='shared_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
