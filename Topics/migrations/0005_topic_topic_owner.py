# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 17:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Topics', '0004_remove_topic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
