"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', views.Test.as_view(), name='chat'),
    path('api/register/', views.Registration.as_view(), name='chat'),
    path('api/auth/', views.Autorization.as_view(), name='chat'),
    path('api/nechetk/', views.Nechetk.as_view(), name='nechetk'),
    path('', views.main, name='main'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('chat/', views.Chat.as_view(), name='register'),
]
