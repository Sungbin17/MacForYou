# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beereview', '0005_beer_overall_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='overall_score',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]