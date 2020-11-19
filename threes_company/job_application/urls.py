from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='jobapp-home'),
    path('apply/<int:job_id>', views.create_job_application, name='jobapp-create'),
    path('edit/', views.edit_job_application, name='jobapp-edit'),
    path('view/', views.view_job_application, name='jobapp-view'),
    path('help/', views.interview_help, name='jobapp-help'),
]