"""pages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import art_upload_view, save_image, published_art_work, upload_at_work

urlpatterns = [
    path('designs/', art_upload_view, name='design'),
    path('save_image/', save_image, name='save_image'),
    path('atwork/', upload_at_work, name='atwork'),
    path('published_art_work/', published_art_work, name='published_art_work'),


]
