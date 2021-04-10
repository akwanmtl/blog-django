from django.conf.urls import url, include

from . import views

app_name = 'blog'
urlpatterns = [
  url(r'^$', views.PostListView.as_view(), name='index'),
  url(r'^add/$', views.add, name='add'),
]
