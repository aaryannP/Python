from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from restaurants.views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')

urlpatterns = [
    path('hello_spotify/', views.hello_spotify, name='hello_spotify'),
    path('music-weather/<str:city>/', views.MusicWeatherAPIView.as_view(), name='music_weather'),
    path('food-location/', views.FoodLocationAPIView.as_view(), name='food_location'),
    path('country-info/<str:country_name>/', views.CountryInfoAPIView.as_view(), name='country_info'),
    path('github-repos/<str:username>/', views.GitHubReposAPIView.as_view(), name='github_repos'),
    path('send-email/', views.SendEmailAPIView.as_view(), name='send_email'),
    path('send-sms/', views.SendSMSAPIView.as_view(), name='send_sms'),
    path('pay/', views.PayAPIView.as_view(), name='pay'),
    path('', include('auth_demo.urls')),
    path('', include(router.urls)),
]



