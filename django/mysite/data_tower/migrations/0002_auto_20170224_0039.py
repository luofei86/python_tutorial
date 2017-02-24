# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_tower', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
        migrations.AddField(
            model_name='article',
            name='articleColumn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_tower.ArticleColumn'),
        ),
        migrations.AddField(
            model_name='articlecolumn',
            name='column_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='column_text',
            field=models.CharField(default='\u672a\u77e5\u5206\u7c7b', max_length=100),
        ),
    ]
