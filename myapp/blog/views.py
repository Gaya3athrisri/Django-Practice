from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse("Helloworld. Index Page")

def detail(request , post_id):
    return HttpResponse(f"you are viewing Post Detail Id of {post_id}")
# Create your views here.

def old_url(request):
    return redirect(reverse('blog:new_url'))

def new_url(request):
    return HttpResponse("Im Newv Url")

def home(request):
    return render(request, 'home.html')

def blog_detail(request,blog_name):
    return render(request,'blog\detail.html')

def post_edit(request,post_id):
    return render(request,'blog\edit.html')