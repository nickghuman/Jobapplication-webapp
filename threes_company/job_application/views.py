# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import JobApplicationForm
from .models import JobApplication

def home(request):
    return render(request, 'job_application/home.html')

def create_job_application(request):
    form = JobApplicationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'job_application/create_job_app.html', context)

def edit_job_application(request):
    return render(request, 'job_application/edit_job_app.html')

def view_job_application(request):
    context = {
        'job_apps': JobApplication.objects.all()
    }
    return render(request, 'job_application/view_job_app.html', context)