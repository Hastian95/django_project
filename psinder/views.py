from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def home(request):
    return render(request, 'psinder/home.html')

def about(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'psinder/about.html',context)

def manyviews(request):

    return render(request, 'psinder/manyviews.html')