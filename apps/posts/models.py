from django.db import models

# Create your models here.
#! 1 models.py - Классы 
#! 2 admin.py - Регистрируем класс
#! 3 views.py - Пишем функцию
# 4 urls.py - Указываем путь где будет работать функция
# 5 templ.html - Выводили данные класса

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
    