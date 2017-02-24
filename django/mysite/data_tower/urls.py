# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


app_name = "data_tower"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artilce/column/$', views.articleColumns, name = "articleColumns"),
    url(r'^artilce/column/add/$', views.addArticleColumn, name = "addArticleColumn"),
    url(r'^artilce/stat/$', views.articleStat, name = "articleStat"),
]
