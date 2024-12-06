from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="blog_index"),
    path("post/<str:post_id>", views.post, name="blog_post"),
    path("detail/<slug:slug>", views.detail,name="blog_detail"),
    path("about/<int:post_id>", views.about, name="blog_about"),
    path("old_url/", views.old_url_redirect, name="blog_old_url"),
    path("new_somthing_url/", views.new_url_view, name="blog_new_url"),
    path('items/', views.item_list, name="blog_item_list"),
    path('create/', views.item_create, name="blog_item_create"),
    path('update/<int:pk>/', views.item_update, name="blog_item_update"),
    path('delete/<int:pk>/', views.item_delete, name="blog_item_delete"),
]
