from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

def home(request):
    return render(request, 'psinder/home.html')

def about(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'psinder/about.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'psinder/about.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def manyviews(request):

    return render(request, 'psinder/manyviews.html')

