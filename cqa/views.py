from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User as AuthUser
from cqa.forms import RegistrationForm

from .models import *

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def home(request):
    context = {}
    context["User"] = request.user.username
    return render(request, "cqa/home.html", context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['errors'] = "Provide valid credentials !!"
            print(username, password, context)
            return render(request, "cqa/login.html", context)
    else:
        return render(request, "cqa/login.html", context)

def signup_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        context['form'] = form
    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'cqa/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request):
    if request.user.is_authenticated:
        posts = Posts.objects.filter(owner_user_id = request.user.id)
        context = {
            'user_id': request.user.account_id,
            'username': request.user.display_name,
            'posts': posts
        }
        return render(request, 'cqa/profile.html', context)
    else:
        return redirect('login')

