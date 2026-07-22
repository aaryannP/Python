from django.urls import path
from .views import SecureAPIView

urlpatterns = [
    path('secure/', SecureAPIView.as_view(), name='secure_api'),
]
