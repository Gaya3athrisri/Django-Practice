from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import Http404
import logging

from .forms import ItemForm
# Get data from db
from .models import Item
from .models import Post


# static data
# posts =[
#          {'id': 1,'title':'Post 1', 'content':'This our 1st Post'},
#          {'id': 2, 'title':'Post 2', 'content':'This our 2nd Post'},
#          {'id': 3, 'title':'Post 3', 'content':'This our 3rd Post'},
#          {'id': 4, 'title':'Post 4', 'content':'This our 4th Post'}
#     ]

def index(request):
    head_title ='Protfolio'
    posts =Post.objects.all()
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

def detail(request, slug):
    #  static data get
    #  post = next((items for items in posts if items['id'] == post_id),None)
    
        try:
            # getting data from DB
            post =Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("Post Does not Exist")
        
        head_tittle ="Post Detail"
        return render(request, 'blog/detail.html',{
           'blog_title':head_tittle,
           'post':post
        })

def old_url_redirect(request):
    return redirect(reverse("new_url"))

def new_url_view(request):
        return HttpResponse("This is you new Redirect Page ")

# List all items
def item_list(request):
    print(request)
    items = Item.objects.all()
    print(items)
    return render(request, 'blog/item_list.html', {'items': items})

# Create a new item
def item_create(request):
    try:
        form = ItemForm()
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog_item_list')
            
        return render(request, 'blog/item_form.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Update an item
def item_update(request, pk):
    item = Item.objects.filter(id = pk).first()
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('blog_item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'blog/item_form.html', {'form': form})

# Delete an item
def item_delete(request, pk):
    item = Item.objects.filter(id = pk).first()
    if request.method == "POST":
        item.delete()
        return redirect('blog_item_list')
    return render(request, 'blog/item_confirm_delete.html', {'item': item})