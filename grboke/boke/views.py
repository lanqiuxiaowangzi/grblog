#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from boke.models import *
from django.core.paginator import *

# Create your views here.
# def index_view(request):
#     return render(request,'index.html')
#分页
def PostPage(request,pindex=1):
    if pindex == '':
        pindex = 1
    list=Post.objects.all()
    paginator = Paginator(list,1)
    page = paginator.page(int(pindex))
    context={'page':page}
    return render(request,'index.html',context)


#阅读全文
def post_details_view(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except:
        pass
    return render(request,'details.html',{'post':post})


def index_guidang(request):
    return render(request,'guidang.html')
def category_details_view(request,category_id=None):
    posts = Post.objects.filter(category=category_id).order_by('-created')
    return render(request,'archive.html',{'posts':posts})


def date_details_view(request,year,month):
    posts = Post.objects.filter(created__year=year,created__month=month).all()
    return render(request,'archive.html',{'posts':posts})












