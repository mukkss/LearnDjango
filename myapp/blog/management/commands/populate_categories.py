
from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This Command Inserts Category  Data"

    def handle(self, *args: Any, **options: Any):
        #Deleteing Exsisting Data
        Category.objects.all().delete()

        categories = ["Technology", "Science", "Art", "Food", "Sports"]

        #Inserting Data
        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))