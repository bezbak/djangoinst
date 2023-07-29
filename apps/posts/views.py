from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.users.models import User
from django.http import HttpResponse
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id') #! === SELECT * FROM post;
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def create_post(request):
    if request.method == 'POST':
        post_image = request.FILES.get('post_image')
        description = request.POST.get('description')
        try:
            post = Post.objects.create(image=post_image, description=description, owner=request.user)
            post.save()
            return redirect('index')
        except:
            return HttpResponse("Не получилось создать пост")
    return render(request, 'create_post.html')

def post_detail(request,id):
    post = Post.objects.get(id = id)
    context = {
        'post':post
    }
    return render(request, 'comment.html', context)

def post_update(request, id):
    post = Post.objects.get(id = id)
    if request.user != post.owner:
        return redirect('index')
    if request.method =="POST":
        image = request.FILES.get('image')
        description = request.POST.get('description')
        if image:
            post.image = image
            post.description = description
        else:
            post.description = description
        post.save()
        return redirect('post_detail',post.id)
    return render(request, 'post_update.html', context={'post':post})

def delete_post(request, id):
    post = Post.objects.get(id = id)
    if request.user != post.owner:
        return redirect('index')
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'post_delete.html', context={'post':post})