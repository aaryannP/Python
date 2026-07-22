from django.urls import path
from . import views

urlpatterns = [
    path('expensive/', views.expensive_view, name='expensive_view'),
    path('manual/', views.manual_cache_view, name='manual_cache_view'),
]
