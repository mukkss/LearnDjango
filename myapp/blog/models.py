from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slugs = models.SlugField(blank=True, null=True)  # Remove unique=True for now


    def save(self, *args, **kwargs):
        self.slugs = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
#Cartegory model
class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name