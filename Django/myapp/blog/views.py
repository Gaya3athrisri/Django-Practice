from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    head_title ='Protfolio'
    posts =[
         {'title':'Post 1', 'content':'This our 1st Post'},
         {'title':'Post 2', 'content':'This our 2nd Post'},
         {'title':'Post 3', 'content':'This our 3rd Post'},
         {'title':'Post 4', 'content':'This our 4th Post'}
    ]
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
     head_tittle ="Post Detail"
     return render(request, 'blog/detail.html',{
          'blog_title':head_tittle,
     })

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_view(request):
        return HttpResponse("This is you new Redirect Page ")