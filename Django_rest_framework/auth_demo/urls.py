from django.urls import path
from . import views

urlpatterns = [
    path('playlists/', views.PlaylistAPIView.as_view(), name='playlists'),
    path('orders/', views.OrderAPIView.as_view(), name='orders'),
    path('cart/', views.CartAPIView.as_view(), name='cart'),
    path('tickets/', views.TicketAPIView.as_view(), name='tickets'),
]
