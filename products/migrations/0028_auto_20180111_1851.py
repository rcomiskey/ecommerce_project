# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20180111_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='product'),
        ),
    ]
