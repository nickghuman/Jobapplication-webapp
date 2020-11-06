from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.home, name='jobapp-home'),
    path(r'^jobapp/create/$', views.create_job_application, name='jobapp-create'),
    path(r'^jobapp/edit/$', views.edit_job_application, name='jobapp-edit'),
]