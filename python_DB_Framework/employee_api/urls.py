from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list_view, name='employee_list'),
    path('employees/create/', views.employee_create_view, name='employee_create'),
]
