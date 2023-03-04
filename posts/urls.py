from django.urls import path
from .views import *

urlpatterns = [
    path('', show_posts.as_view(), name='show_posts'),
    path('<int:pk>/', detail_post.as_view(), name='detail_post'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('answer/<int:post_id>/', answer_post, name='answer_post'),
]
