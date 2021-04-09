from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.

def index(request):
  return render(request, 'blog/index.html', {
    'header' : 'Hello this is a blog'
  })

def add(request):
  return render(request, 'blog/add.html', {'form': PostForm()})