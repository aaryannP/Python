from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.AdvancedEmployeeViewSet, basename='advanced-employee')

urlpatterns = [
    path('', include(router.urls)),
]
