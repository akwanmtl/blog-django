from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.utils import timezone
from django.forms.models import model_to_dict
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

def edit(request, post_id):
  print(request.method)
  if request.method == "POST":
    form = PostForm(request.POST)
    
    if form.is_valid():
      updatedPost = Post.objects.get(id=post_id)
      updatedPost.title = form.cleaned_data["title"]
      updatedPost.body = form.cleaned_data["body"]
      updatedPost.save()
    
      # Post.objects.filter(id=post_id).update(title=form.cleaned_data["title"], body=form.cleaned_data["body"])
      # print('valid')
      return redirect("blog:index")
    
    else:
      # print('invalid')
      return render(request, 'blog/edit.html', {'form' : form, "id":post_id})

  else:

    updatedPost = Post.objects.get(id=post_id)
    print(updatedPost.title)
    updateForm = PostForm(initial=model_to_dict(updatedPost))
    context = { 'header' : 'GET', 'form' : updateForm, "id":post_id }

    return render(request, 'blog/edit.html', context)

    
def delete(request, post_id):
  if request.method == "DELETE":
    print(request.method)
    print(post_id)
    post = get_object_or_404(Post, id=post_id)
    
    Post.objects.filter(id=post_id).delete()
    return HttpResponse(status=204)

  else:
    return redirect("blog:index")
  
    

  