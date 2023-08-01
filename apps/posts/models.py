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
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name= 'comment_user', on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name= 'comment_post', on_delete = models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.text


class Like(models.Model):
    user = models.ForeignKey(User, related_name= 'user_like', on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name= 'post_like', on_delete = models.CASCADE)