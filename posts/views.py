from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from cqa.models import *
from posts.forms import CreatePost, EditPost, AnswerPost
from django.shortcuts import redirect
from django.http import HttpResponse
    
def home(request):
    posts = Posts.objects.filter().exclude(title=None)[0:10]
    context = {'posts': posts}
    return render(request, 'posts/home.html', context)

def detail_post(request, post_id):
    post = Posts.objects.filter(id=post_id)[0]
    answers = Posts.objects.filter(parent_id=post_id)
    user = CustomUser.objects.filter(id = post.owner_user_id)
    if user.count() == 0:
        username = ''
    else:
        username = user[0].username
    context = {
        'post': post,
        'answers': answers,
        'username': username
    }
    return render(request, 'posts/detail_post.html', context)
    pass

# class detail_post(DetailView):
#     template_name = 'posts/detail_post.html'
#     model = Posts
#     ordering = ['-creation_date']
#     context_object_name = 'post'
    
#     def get_context_data(self, *args, **kwargs):
#         qs = super(detail_post, self).get_context_data(*args, **kwargs)
#         # qs['user'] = "hallo"
#         # print(type(self.request.user.display_name))
#         return qs


def create_post(request):
    global context
    if not request.user.is_authenticated:
        redirect('home')

    if request.method == 'POST':
        form = CreatePost(request.POST)
        user = request.user
        if form.is_valid():
            object = Posts()
            object.owner_user_id = user.id
            object.post_type_id = '1'
            object.answer_count = 0
            object.comment_count = 0
            object.owner_display_name = user.display_name
            object.title = form.cleaned_data['title']
            object.tags = form.cleaned_data['tags']
            tags = form.cleaned_data['tags'].split(',')
            tags = [tag[1:] for tag in tags]
            tags = [ '<' + tag.strip() + '>' for tag in tags ]
            object.tags = ''.join(tags)
            object.content_license='CC BY SA 2.5'  # dummy value
            object.body = form.cleaned_data['body']
            # TO DO: insert the corresponding fields into the tags table as well
            object.score = 0 # dummy
            
            object.save()
            # redirect to a detail view of the post you just created instead
            return redirect('profile')


    new_post = CreatePost()
    context["form"] = new_post
    return render(request, 'posts/creation_form.html', context)

def edit_post(request, post_id):
    global context
    if not request.user.is_authenticated:
        redirect('home')

    curr_post = Posts.objects.get(id=post_id)
    user = request.user

    # Checking if the user is the owner of the post
    if curr_post.owner_user_id != user.account_id:
        redirect('home')

    if request.method == 'POST':
        form = EditPost(curr_post, request.POST)
        if form.is_valid():
            print('Hello')
            curr_post.title = form.cleaned_data['title']
            curr_post.body = form.cleaned_data['body']
            # curr_post.tags = form.cleaned_data['tags']
            tags = form.cleaned_data['tags'].split(',')
            tags = [ '<' + tag.strip() + '>' for tag in tags ]
            curr_post.tags = ''.join(tags)
            curr_post.save()
            return redirect('home')
        else:
            print('bonk')
            print(form.errors)
            print(form.non_field_errors)
    
    form = EditPost(curr_post)
    context["form"] = form
    context["post_id"] = post_id
    # context = {'form': form, 'post_id': post_id}
    return render(request, 'posts/edit_form.html', context)


def answer_post(request, post_id):

    if not request.user.is_authenticated:
        redirect('home')
    
    curr_post = Posts.objects.get(id = post_id) 
    user = request.user

    if request.method == 'POST':
        form = AnswerPost(request.POST, curr_post)
        if form.is_valid():
            object = Posts()

            object.owner_user_id = user.id
            object.post_type_id = '2'
            object.answer_count = 0
            if not curr_post.answer_count:
                curr_post.answer_count = 0
            curr_post.answer_count += 1

            object.comment_count = 0
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
