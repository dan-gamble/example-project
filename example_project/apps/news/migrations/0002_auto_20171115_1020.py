# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='per_page',
            field=models.IntegerField(default=12, verbose_name='Articles per page'),
        ),
    ]
