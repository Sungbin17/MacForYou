# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofiles_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofiles',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='number_of_posts',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='score',
        ),
    ]