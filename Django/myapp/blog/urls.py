from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path("", views.index, name="index" ),
    path("post/<str:post_id>", views.post, name="post"),
    path("detail/<int:post_id>", views.detail,name="detail"),
    path("about/<int:post_id>", views.about, name="about"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("new_somthing_url", views.new_url_view, name="new_url")
]
