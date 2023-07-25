from django.db import models
from apps.users.models import User
# Create your models here.

class Post(models.Model):
    image = models.ImageField(
        upload_to='post_images/'
    )
    description = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.description[:15]
    