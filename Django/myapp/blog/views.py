from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.

posts =[
         {'id': 1,'title':'Post 1', 'content':'This our 1st Post'},
         {'id': 2, 'title':'Post 2', 'content':'This our 2nd Post'},
         {'id': 3, 'title':'Post 3', 'content':'This our 3rd Post'},
         {'id': 4, 'title':'Post 4', 'content':'This our 4th Post'}
    ]

def index(request):
    head_title ='Protfolio'
    return render(request, 'blog/index.html',{
         'blog_title': head_title,
          'posts': posts
    })

def post(request, post_id):
    return HttpResponse(f"You are at Blog Detail Page and the post Id is {post_id}")

def about(request, post_id):
     head_tittle ="About Me"
     return render(request, 'blog/about.html',{
          'blog_title':head_tittle,
     })

def detail(request, post_id):
     post = next((items for items in posts if items['id'] == post_id),None)
     head_tittle ="Post Detail"
     return render(request, 'blog/detail.html',{
          'blog_title':head_tittle,
          'post':post
     })

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_view(request):
        return HttpResponse("This is you new Redirect Page ")