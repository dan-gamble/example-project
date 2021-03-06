# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='legal_link',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='terms_of_use_link',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='text',
        ),
        migrations.AddField(
            model_name='footer',
            name='about_text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='footer',
            name='about_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='footer',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='address_link_page',
            field=models.ForeignKey(blank=True, help_text='If you want to link to an internal page, please use this.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.Page', verbose_name='Link page'),
        ),
        migrations.AddField(
            model_name='footer',
            name='address_link_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Link text'),
        ),
        migrations.AddField(
            model_name='footer',
            name='address_link_url',
            field=models.CharField(blank=True, help_text='If you want to link to an external page, please use this.', max_length=200, null=True, verbose_name='Link URL'),
        ),
        migrations.AddField(
            model_name='footer',
            name='address_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='footer',
            name='legal_page',
            field=models.ForeignKey(blank=True, help_text='If you want to link to an internal page, please use this.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='footer',
            name='legal_text',
            field=models.CharField(blank=True, default='Legal', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='legal_url',
            field=models.CharField(blank=True, help_text='If you want to link to an external page, please use this.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='links_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='footer',
            name='privacy_policy_text',
            field=models.CharField(blank=True, default='Privacy Policy', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='privacy_policy_url',
            field=models.ForeignKey(blank=True, help_text='If you want to link to an internal page, please use this.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='footer',
            name='terms_of_use_page',
            field=models.ForeignKey(blank=True, help_text='If you want to link to an internal page, please use this.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='footer',
            name='terms_of_use_text',
            field=models.CharField(blank=True, default='Terms of use', max_length=255, null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='footer',
            name='terms_of_use_url',
            field=models.CharField(blank=True, help_text='If you want to link to an external page, please use this.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='privacy_policy_link',
            field=models.CharField(blank=True, help_text='If you want to link to an external page, please use this.', max_length=255, null=True),
        ),
    ]
