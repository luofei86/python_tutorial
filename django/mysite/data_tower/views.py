# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.urls import reverse

from .models import Article
from .models import ArticleColumn
from .models import ArticleStat
from .models import ArticleStatDetail


# Create your views here.

def index(request):
	return render(request, 'data_tower/index.html', {})

# class IndexView(ListView):

def addArticleColumn(request):
	articleColumnId = request.POST['articleColumnId']
	articleColumnText = request.POST['articleColumnText']
	articleColumn = ArticleColumn()
	articleColumn.column_id = articleColumnId
	articleColumn.column_text = articleColumnText
	articleColumn.save()
	return HttpResponseRedirect(reverse('data_tower:articleColumns'))

def articleColumns(request):
	articleColumns = ArticleColumn.objects.all()
	return render(request, "data_tower/article_columns.html", {'articleColumns': articleColumns})

def articleStat(request, articeId):
	if articeId:
		articleStats = ArticleStat.objects.filter(article_id = articeId)
	else:
		articleStats = ArticleStat.objects.order_by("-views")[:10]
	return render(request, "data_tower/article_stat.html", {'articleStats': articleStats})
