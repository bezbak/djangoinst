from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(
        upload_to='post_images/'
    )
    description = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.description[:15]
    