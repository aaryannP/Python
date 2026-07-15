from django.urls import path
from . import views

urlpatterns = [
    # APIView endpoints
    path('apiview/', views.RestaurantListCreateAPIView.as_view(), name='apiview-list-create'),
    path('apiview/<int:pk>/', views.RestaurantDetailAPIView.as_view(), name='apiview-detail'),
    
    # GenericAPIView with Mixins endpoints
    path('generic/', views.RestaurantGenericListCreateView.as_view(), name='generic-list-create'),
    path('generic/<int:pk>/', views.RestaurantGenericDetailView.as_view(), name='generic-detail'),
]
