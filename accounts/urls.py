"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to uprofilerlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index
# from .views import account_detail_view, userprofile_view, dynamic_lookup_view, signup_view, CreateUserProfileView
from .views import account_detail_view, signup_view
from . import views

urlpatterns = [
    # path('', index),
    path('signup/', signup_view, name='signup'),

    # path('', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('profile/', account_detail_view, name='profile'),

    path('going_to_save_account/', views.going_to_save_account, name="going_to_save_account"),
    path('going_to_save_all_info/', views.going_to_save_all_info, name="going_to_save_all_info"),
    path('delete_this/<int:pk_id>', views.delete_this, name="delete_this"),


    # path('', views.first_login_page, name='first_login_page'),
    path('', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('login_redirect_from_logout/', views.login_redirect_from_logout, name='login_redirect_from_logout'),


]
