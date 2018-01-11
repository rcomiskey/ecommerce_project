# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 18:00
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20171219_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeManyToManyField(blank=True, db_index=True, related_name='_category_parent_+', to='products.Category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeManyToManyField(to='products.Category'),
        ),
    ]
