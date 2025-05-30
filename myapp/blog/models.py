from django.db import models


class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
# Create your models here.

class Blog(models.Model):
    tittle =models.CharField(max_length=50)
    discription = models.TextField()
    price =models.DecimalField(max_digits=10,decimal_places=2)
    

    def __str(self):
        return self.tittle