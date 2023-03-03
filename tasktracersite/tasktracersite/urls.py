"""
tasktracersite URL Configuration

What we have:
admin/ - admin panel
api/ - URL from app/urls.py
auth/token/ - get token
auth/refresh - refresh token

Check also: app/urls.py
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('auth/token', TokenObtainPairView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
]
