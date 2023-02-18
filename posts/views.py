from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

# app_name = 'posts'
# Create your views here.

# def show_posts(request):
#     context  =  {}
    
# 
#return render(request, 'show_posts.html')

class show_posts(ListView):
    template_name = 'posts/show_posts.html'
    model = Posts
    ordering = ['-creation_date']
    paginate_by = 10
    context_object_name = 'posts'
    
    def get_query_set(self, *args, **kwargs):
        qs = super(show_posts, self).get_query_set(*args, **kwargs)
        print(qs)
        return qs