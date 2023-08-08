from django.shortcuts import render, redirect
from apps.posts.models import Post, Comment, Like
from django.db.models import Q
from apps.users.models import User, Follower
from django.http import HttpResponse
# Create your views here.
def index(request):
    follow_users = Follower.objects.all().filter(from_user = request.user) #! Запрашиваем наши подписки
    follow_users = [i.to_user for i in follow_users]
    follow_posts = Post.objects.all().filter(owner__in=follow_users) #! ЗАпрашиваем посты наших подписок
    posts = Post.objects.all().exclude(owner__in = follow_users).order_by('?')[:10] #! === SELECT * FROM post;
    if request.method == 'POST':
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)
        try:
            like = Like.objects.get(post = post, user = request.user)
            like.delete()
            return redirect('index')
        except:
            like = Like.objects.create(post=post, user = request.user)
            return redirect('index')
    context = {
        'posts':posts,
        'follow_posts':follow_posts
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
    if request.method == 'POST':
        if 'comment' in request.POST:
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post, user = request.user, text = text)
            comment.save()
            return redirect('post_detail', post.id)
        if 'like' in request.POST:
            try:
                like = Like.objects.get(post = post, user = request.user)
                like.delete()
                return redirect('post_detail', post.id)
            except:
                like = Like.objects.create(post=post, user = request.user)
                return redirect('post_detail', post.id)
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

def search(request):
    search_key = request.GET.get('search_key')
    posts = Post.objects.all()
    users = User.objects.all()
    if search_key:
        posts = Post.objects.all().filter(Q(description__icontains = search_key))
        users = User.objects.all().filter(Q(username__icontains = search_key))
    context = {
        'posts':posts,
        'users':users,
    }
    return render(request, 'search.html', context)