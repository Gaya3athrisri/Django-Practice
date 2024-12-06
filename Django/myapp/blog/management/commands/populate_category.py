from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand 


class Command(BaseCommand):
    help = " This command insert category data"

    def handle(self, *args: Any, **options: Any):
        #Delete exsiting data
        Category.objects.all().delete()

        categories=[
            "Life",
            "Science",
            "Tech"
            ]

       


        for category_name in categories:
            Category.objects.create(name=category_name)
        
        self.stdout.write(self.style.SUCCESS("Complete inserting Data!"))