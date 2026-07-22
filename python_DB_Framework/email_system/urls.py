from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='email_home'),
    path('reset-password/', views.trigger_password_reset, name='trigger_password_reset'),
    path('order-confirm/', views.send_order_confirmation, name='send_order_confirmation'),
    path('ipl-welcome/', views.send_ipl_welcome, name='send_ipl_welcome'),
]
