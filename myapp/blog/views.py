from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Blog

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
    title = "Blog Detail"
    return render(request,'blog\detail.html' , {'title':title})

def post_edit(request,post_id):
    if request.method == 'POST':
        tittle = request.POST['itemTitle']
        discription = request.POST['itemDescription']
        price = request.POST['itemPrice']

        if Blog.objects.filter(tittle=tittle):
            message ='We have already have this Tittle , Enter the another One.'
            return render(request, 'blog/alert.html', {'message': message})
        
        blog = Blog( tittle=tittle , discription= discription , price=price)
        blog.save()
        return render(request,'blog/alert.html',{'message': message})

    return render(request,'blog\edit.html')

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render()) 

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render()) 