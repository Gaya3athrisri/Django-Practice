from django.db import models


class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
# Create your models here.

class Blog(models.Model):
    item_tittle =models.CharField(max_length=50)
    item_discription = models.TextFeild()