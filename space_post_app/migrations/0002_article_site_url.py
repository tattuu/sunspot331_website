# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_post_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='site_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]