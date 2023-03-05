from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from posts.forms import CreatePost, EditPost, AnswerPost
from django.shortcuts import redirect
from django.http import HttpResponse

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

            # TO DO: insert the corresponding fields into the tags table as well
            object.score = 0 # dummy
            
            object.save()
            return redirect('show_posts')


    new_post = CreatePost()
    context = {'form': new_post}
    return render(request, 'posts/creation_form.html', context)

def edit_post(request, post_id):

    curr_post = Posts.objects.get(id=post_id)

    # TO DO: check if the owner of the post is the logged in user

    if request.method == 'POST':
        form = EditPost(curr_post, request.POST)
        if form.is_valid():
            print('Hello')
            curr_post.title = form.cleaned_data['title']
            curr_post.body = form.cleaned_data['body']
            curr_post.tags = form.cleaned_data['tags']
            curr_post.save()
            return redirect('show_posts')
        else:
            print('bonk')
            print(form.errors)
            print(form.non_field_errors)
    
    form = EditPost(curr_post)
    context = {'form': form, 'post_id': post_id}
    return render(request, 'posts/edit_form.html', context)


def answer_post(request, post_id):
    curr_post = Posts.objects.get(id = post_id) 
    if request.method == 'POST':
        form = AnswerPost(request.POST, curr_post)
        if form.is_valid():
            object = Posts()

            object.owner_user_id = 42 # dummy
            object.post_type_id = '2'
            object.answer_count = 0
            if not curr_post.answer_count:
                curr_post.answer_count = 0
            curr_post.answer_count += 1

            object.comment_count = 0
            object.owner_user_id = 42  # dummy val
            object.tags = curr_post.tags
            object.content_license = curr_post.content_license
            object.parent_id = curr_post.pk
            object.title = "[Answer]" + curr_post.title
            object.body = form.cleaned_data['body']

            object.score = 0

            object.save()
            return redirect('detail_post', pk=object.pk)

    form = AnswerPost()
    context = {'form': form, 'post_id': post_id,}
    return render(request, 'posts/answer_form.html', context)
