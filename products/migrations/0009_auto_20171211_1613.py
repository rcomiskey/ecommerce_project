# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 16:13
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20171211_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parents',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeManyToManyField(blank=True, db_index=True, null=True, related_name='_category_parent_+', to='products.Category'),
        ),
    ]