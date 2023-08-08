from django.urls import path
from .views import index, create_post, post_detail, post_update, delete_post, search
urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create_post'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('post_update/<int:id>/', post_update, name='post_update'),
    path('delete_post/<int:id>/', delete_post, name='delete_post'),
    path('search/', search, name='search'),
]
