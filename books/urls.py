from django.contrib import admin
from django.urls import path, include
from app import views as app_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
