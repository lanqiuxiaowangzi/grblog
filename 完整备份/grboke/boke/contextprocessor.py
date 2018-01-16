#coding=UTF-8
from boke.models import *
from datetime import date
from django.db.models import *
def slider_context_processor(request):
    context = {}
    #分类
    context['category']=Post.objects.values('category','category__name').annotate(count=Count('*'))
    #归档 获取时间并按时间降序分组
    archive = Post.objects.values('created').order_by('-created')
    context['archive']=archive
    #近期文章 按时间降序分组显示前5个
    context['recent']=Post.objects.order_by('-created').all()[:5]
    return context









