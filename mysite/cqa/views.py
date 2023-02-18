from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User as AuthUser

def index(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hello, world. You're at the polls index.{request.user}")
    else:
        return redirect('login')


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['errors'] = "Provide valid credentials !!"
            print(username, password, context)
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)

def signup_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = AuthUser.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            context['errors'] = "Provide valid credentials !!"
            return render(request, "signup.html", context)
    else:
        return render(request, "signup.html", context)