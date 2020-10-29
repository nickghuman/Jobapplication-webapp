from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='jobapp-home'),
    url(r'^jobapp/create/$', views.create_job_application, name='jobapp-create'),
    url(r'^jobapp/edit/$', views.edit_job_application, name='jobapp-edit'),
]