import random
from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand 



class Command(BaseCommand):
    help = " This command insert post data"

    def handle(self, *args: Any, **options: Any):
        #Delete exsiting data
        Post.objects.all().delete()

        titles=[
            "Dogs",
            "Plants",
            "City",
            "Sea",
            "Decision",
            "OCD",
            "Alone in City"
            ]

        content= [
            'The dog was the first animal domesticated by man. It is a mammal. It learned to live with humans less than 14,000 years ago. If you look at the ancient remains found in Denmark, Germany, China and Japan, you will understand the importance of dog in those days. Dogs are very faithful animal. ',
            'Planting plants means providing shade and health to the present and future generations. According to the Padma Purana, those who plant the plants will reach heaven after death. ",',
            'A city is a human settlement of a substantial size. The term  city  has different meanings around the world and in some places the settlement can be very ...',
            'A sea is a large body of salt water. There are particular seas and the sea. The sea commonly refers to the Ocean, the interconnected body of seawaters that spans most of Earth. Particular seas are either marginal seas, second-order sections of the oceanic sea (e.g. the Mediterranean Sea), or certain large, nearly landlocked bodies of water.',
            'In psychology, decision-making (also spelled decision making and decisionmaking) is regarded as the cognitive process resulting in the selection of a belief or a course of action among several possible alternative options. It could be either rational or irrational. The decision-making process is a reasoning process based on assumptions of values, preferences and beliefs of the decision-maker.Every decision-making process produces a final choice, which may or may not prompt action.',
            'Obsessive-compulsive disorder (OCD) is a long-lasting disorder in which a person experiences uncontrollable and recurring thoughts (obsessions), engages in repetitive behaviors (compulsions), or both. People with OCD have time-consuming symptoms that can cause significant distress or interfere with daily life.',
            'You can try focusing on your reason for such a bold move. Consider that this loneliness wont last forever. You will meet new people and soon have new friends who may end up close as family. Always remain focused and try not to remain ideal. In your free time when not studying, you can engage in some self care. You can also visit inexpensive places like the park or museum. Soon you will get over this, connect with others as well.',

        ]

        img_url =[
            "https://picsum.photos/id/494/600/400",       
            "https://picsum.photos/id/237/600/400",
            "https://picsum.photos/id/376/600/400",
            "https://picsum.photos/id/92/600/400",
            "https://picsum.photos/id/69/600/400",
            "https://picsum.photos/id/60/600/400",
            "https://picsum.photos/id/43/600/400"
                ]

        categories = Category.objects.all()
        for title, content, img_url in zip(titles, content, img_url):
            categorys = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url,category= categorys)
        
        self.stdout.write(self.style.SUCCESS("Complete inserting Data!"))