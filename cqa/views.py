from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User as AuthUser
from django.views.generic.list import ListView
from .models import *

def index(request):
    if request.user.is_authenticated:
        return render(request, "base.html", {})
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = AuthUser.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            context['errors'] = "Provide valid credentials !!"
            return render(request, "cqa/signup.html", context)
    else:
        return render(request, "cqa/signup.html", context)

       
# class HomeView(ListView):
#     #render all posts of this particular user
#     model = Posts
#     context_object_name = 'posts'
#     template_name = 'cqa/home.html'
#     ordering = ['-creation_date']
#     paginate_by = 10
#     context_object_name = 'user_posts'
    
    
#     def get_query_set(self ,*args, **kwargs):
#         # posts = super(HomeView, self).get_query_set(self, *args, **kwargs)
#         # user = Users.objects.get(user_id = self.request.user.id)
#         # print(user)
#         # posts = posts.filter(owner_user_id = user.owner_user_id)
#         posts = []
#         return posts
