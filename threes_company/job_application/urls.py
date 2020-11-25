from django.urls import path
from . import views
from register import views as register_views

urlpatterns = [
    path('job_dashboard/', views.home, name='jobapp-home'),
    path('apply/<int:job_id>/', views.create_job_application, name='jobapp-create'),
    path('edit/<int:job_app_id>/', views.edit_job_application, name='jobapp-edit'),
    path('view/', views.view_job_application, name='jobapp-view'),
    path('help/', views.interview_help, name='jobapp-help'),
    path('delete/<job_id>', views.delete_job_application, name='jobapp-delete'),
]