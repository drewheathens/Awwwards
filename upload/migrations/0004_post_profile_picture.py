# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-20 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_remove_post_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/profilephotos/'),
            preserve_default=False,
        ),
    ]
