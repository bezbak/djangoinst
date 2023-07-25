from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from apps.users.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('username')
        if password == confirm_password:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return redirect('register')
    return render(request, 'register.html')