from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from posts.forms import CreatePost
from django.shortcuts import redirect

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


class detail_post(DetailView):
    template_name = 'posts/detail_post.html'
    model = Posts
    ordering = ['-creation_date']
    context_object_name = 'post'
    
    def get_context_data(self, *args, **kwargs):
        qs = super(detail_post, self).get_context_data(*args, **kwargs)
        # qs['user'] = "hallo"
        # print(type(self.request.user.display_name))
        return qs


def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            object = Posts()
            object.owner_user_id = 10 # dummy value
            object.post_type_id = '1'
            object.answer_count = 0
            object.comment_count = 0
            object.owner_display_name = 'Fuji KN'
            object.title = form.cleaned_data['title']
            object.tags = form.cleaned_data['tags']
            object.content_license='CC BY SA 2.5'  # dummy value
            object.body = form.cleaned_data['body']

            object.score = 0 # dummy
            
            object.save()
            return redirect('show_posts')


    new_post = CreatePost()
    context = {'form': new_post}
    return render(request, 'posts/creation_form.html', context)
