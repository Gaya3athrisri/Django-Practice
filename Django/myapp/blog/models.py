from django.db import models
from django.utils.text import slugify

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name= models.CharField(max_length=20)
   
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content =models.TextField()
    img_url =models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug =models.SlugField(null=False)
    Category =models.ForeignKey(Category , on_delete=models.CASCADE)

    def save( self, *args, **kwargs ):
        self.slug = slugify (self.title)
        super().save( *args, **kwargs)

    def __str__(self):
        return self.title

