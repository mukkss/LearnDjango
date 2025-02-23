from django.db import models


# Create your models here.
class Post(models.Model):
    def __init__(self):
        pass
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title