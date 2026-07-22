from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='cbv_home'),
    path('about/', views.AboutUsView.as_view(), name='cbv_about'),
    path('api/courses/', views.CourseAPIView.as_view(), name='api_courses'),
    path('contact/', views.ContactView.as_view(), name='cbv_contact'),
]
