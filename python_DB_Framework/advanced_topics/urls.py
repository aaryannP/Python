from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='advanced_home'),
    path('books/', views.book_list_view, name='book_list'),
]
