from django.urls import path
from .views import *

urlpatterns = [
    path('', show_posts.as_view(), name='show_posts'),
    path('<int:pk>/', detail_post.as_view(), name='detail_post'),
]