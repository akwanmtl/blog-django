from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.views.generic import ListView

# Create your views here.

# def index(request):
#   return render(request, 'blog/index.html', {
#     'header' : 'Hello this is a blog'
#   })

class PostListView(ListView):
  model = Post
  template_name = 'blog/index.html'

  def get_context_data(self, **kwargs):
    context = super(PostListView, self).get_context_data(**kwargs)
    # print(context)
    # context['created'] = timezone.localtime(context['created'])

    return context

def add(request):

  if request.method == "POST":
    form = PostForm(request.POST)
    
    if form.is_valid():
      Post(
        title=form.cleaned_data["title"],
        body=form.cleaned_data["body"]
      ).save()

      return redirect("blog:index")
    
    else:
      return render(request, 'blog/add.html', {'form' : form})

  else:

    context = { 'header' : 'GET', 'form' : PostForm() }

    return render(request, 'blog/add.html', context)