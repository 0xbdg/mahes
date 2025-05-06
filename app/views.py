from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    return render(request,"pages/index.html", context={})

def article(request):
    item = Blog.objects.all()
    return render(request, "pages/article.html", context={"items": item})

def article_detail(request, slug):

    item = Blog.objects.get(slug=slug)
    return render(request, "pages/article_detail.html", context={"page": item})

def member(request):
    return render(request, "pages/member.html", context={})
