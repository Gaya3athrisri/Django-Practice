from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.index, name="index" ),
    path('home', views.home, name='name'),
    path("blog_detail/<str:blog_name>", views.blog_detail, name="blog_detail"),
    path("post_edit/<int:post_id>", views.post_edit, name="post_edit"),
    path("detail/<int:post_id>" , views.detail, name="detail"),
    path("old_some_url", views.old_url, name='old_url'),
    path("new_url", views.new_url, name='new_url'),
    path('about', views.about, name='about')
]
