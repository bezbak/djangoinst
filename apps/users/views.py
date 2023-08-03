from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from apps.users.models import User
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
                return redirect("index")
            
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
    context = {
        'user':user
    }
    return render(request, 'my_account.html', context)