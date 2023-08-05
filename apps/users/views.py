from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from apps.users.models import User, Follower
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if len(password) >= 8:
                user = User.objects.create(username=username)
                user.set_password(password)
                user.save()
                user = User.objects.get(username = username)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("profile_update", user.username)
            
            else:
                return HttpResponse("Пароль слишком похож на Аяну")
        else:
            return HttpResponse("Пароли не совпадают")
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        except:
            return HttpResponse('Такого пользователя нет')
    return render(request, 'sign-in.html')

def profile(request, username):
    user = User.objects.get(username=username)
    follow_status = Follower.objects.all().filter(from_user = request.user, to_user = user).exists()
    if request.method == "POST":
        try:
            follow = Follower.objects.get(from_user = request.user, to_user = user)
            follow.delete()
            return redirect("profile",user.username)
        except:
            follow = Follower.objects.create(from_user = request.user, to_user = user)
            return redirect("profile",user.username)
    context = {
        'user':user,
        'follow_status':follow_status,
    }
    return render(request, 'my_account.html', context)

def profile_update(request,username):
    user = User.objects.get(username = username)
    
    context = {
        'user':user
    }
    if request.user != user:
        return redirect("index")
    if request.method=='POST':
        photo=request.FILES.get("image")
        descr=request.POST.get('descr')
        name=request.POST.get('username')
        if photo:
            user.profile_image=photo
            user.description=descr
            user.username=name
            user.save()
            return redirect("profile",user.username)
        else:
            user.description=descr
            user.username=name
            user.save()
            return redirect("profile",user.username)
    return render(request,"profile_update.html",context)