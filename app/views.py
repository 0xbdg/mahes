from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"pages/index.html", context={})

def article(request):
    return render(request, "pages/article.html", context={})
