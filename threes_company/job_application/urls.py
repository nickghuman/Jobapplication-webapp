from django.urls import path
from . import views
from register import views as register_views

urlpatterns = [
    path('jobapp/home/', views.home, name='jobapp-home'),
    path('jobapp/create/', views.create_job_application, name='jobapp-create'),
    path('jobapp/edit/', views.edit_job_application, name='jobapp-edit'),
    path('jobapp/view/', views.view_job_application, name='jobapp-view'),
]