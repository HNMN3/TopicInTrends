# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 19:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Topics', '0006_auto_20170401_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commented_on',
            new_name='comment_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='topic',
            new_name='comment_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='total_comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]