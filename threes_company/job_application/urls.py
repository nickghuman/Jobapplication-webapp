from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='jobapp-home'),
    path('jobapp/create/', views.create_job_application, name='jobapp-create'),
    path('jobapp/edit/', views.edit_job_application, name='jobapp-edit'),
]