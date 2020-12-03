from django.conf.urls import url
from . import views
from django.contrib.auth.models import User
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

  path('', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
  path('sign_in/',auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
  path('logout/' ,auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
  path('register/' , views.register, name='register'),
  path('profile/', views.profile, name='profile'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
  path('create_profile/', views.create_profile, name='create_profile'),
]

