from django.shortcuts import render
from .models import Blog
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def newpost(request):
    return render(request, 'newpost.html')

def all(request):
    return render(request,'all.html')

def allsearch(request):
    blogs=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        blogs=Blog.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'cat.html',{'query':query,'blogs':blogs})