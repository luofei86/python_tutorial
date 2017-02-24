# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class ArticleColumn(models.Model):
	column_id = models.IntegerField(default=0)
	column_text = models.CharField(max_length = 100, default="未知分类")

	# def __init__(self):
	# 	self.column_id = 0

	# def __init__(self, column_id, column_text):
	# 	self.column_id = column_id
	# 	self.column_text = column_text

	def __str__(self):
		return self.column_text

@python_2_unicode_compatible
class Article(models.Model):
	articleColumn = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, null = True, name="article_column")
	article_title = models.CharField(max_length=500)
	article_url = models.CharField(max_length = 1000)

	def __str__(self):
		return self.article_title


@python_2_unicode_compatible
class ArticleStat(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	views = models.IntegerField(default = 0)

	def __str__(self):
		toString = "Articel: %s, Views: %d" % (self.column_text, self.views)
		return toString

@python_2_unicode_compatible
class ArticleStatDetail(models.Model):
	article_id = models.IntegerField(default = 0)
	stat_data = models.DateTimeField('stat collect')
	views = models.IntegerField(default = 0)

	def __str__(self):
		toString = "Articel: %s, Current Views: %d" % (self.column_text, self.views)
		return toString