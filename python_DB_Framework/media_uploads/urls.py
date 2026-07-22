from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list_view, name='profile_list'),
    path('upload/', views.upload_profile_view, name='upload_profile'),
]
