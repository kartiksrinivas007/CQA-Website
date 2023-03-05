from django.urls import path
from .views import search_view, search_results_view

urlpatterns = [
    path('', search_view, name = 'search_view'),
    path('results/<str:search>', search_results_view.as_view(), name = 'search_results'),
]