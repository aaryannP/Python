"""
URL configuration for python_DB_Framework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('session2/', include('playlists.urls')),
    path('session3/', include('templates_demo.urls')),
    path('session4/', include('foodiespot.urls')),
    path('session5/', include('admin_panel.urls')),
    path('session6/', include('forms_demo.urls')),
    path('session7/', include('modelform_demo.urls')),
    path('session8/', include('authentication.urls')),
    path('session9/', include('email_system.urls')),
    path('session10/', include('otp_system.urls')),
    path('session11/', include('cbv_demo.urls')),
    path('session12/', include('crud_app.urls')),
    path('session13/', include('advanced_topics.urls')),
    path('session14/', include('media_uploads.urls')),
    path('api/session15/', include('employee_api.urls')),
    path('api/session16/', include('advanced_api.urls')),
    path('api/session17/', include('jwt_auth_demo.urls')),
    path('api/session18/', include('drf_advanced.urls')),
    path('session19/', include('cache_demo.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
