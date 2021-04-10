from django.conf.urls import url, include

from . import views

app_name = 'blog'
urlpatterns = [
  # url(r'^$', views.PostListView.as_view(), name='index'),
  url(r'^$', views.index, name='index'),
  url(r'^add/$', views.add, name='add'),
  url(r'^delete/(?P<post_id>[0-9]+)/$', views.delete, name='delete'),
  url(r'^edit/(?P<post_id>[0-9]+)/', views.edit, name='edit'),
]
