# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_calltoaction_link_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calltoaction',
            old_name='super_title',
            new_name='kicker',
        ),
    ]