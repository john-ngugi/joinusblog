from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.

def blogs(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-created_on')
    return render(request, "blogs.html", {'posts':posts})

def postDetail(request,slug):
    post = Post.objects.get(slug = slug)
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-created_on')[1:4]
    return render(request,"blogpost.html",{'post':post,'posts':posts})

def intro(request):
    data1 = Post.objects.first()
    return render(request, "index.html", {'data':data1})

def blogpost1(request):
    post1=Post.objects.first()
    return render(request, "blogpost1.html", {'data1':post1})

def aboutus(request):
    return render(request,'aboutus.html')    

