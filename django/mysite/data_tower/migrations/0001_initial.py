# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('article_title', models.CharField(max_length=500)),
                ('article_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_tower.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleStatDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField(default=0)),
                ('stat_data', models.DateTimeField(verbose_name='stat collect')),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
