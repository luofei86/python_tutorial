# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_articlecolumn'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleColumn',
        ),
    ]