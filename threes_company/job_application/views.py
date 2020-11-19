# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import JobApplicationForm
from .models import JobApplication
from .models import JobPosting

def home(request):
    context = {
        'job_postings': JobPosting.objects.all()
    }
    return render(request, 'job_application/home.html', context)

def create_job_application(request, job_id):
    form = JobApplicationForm(request.POST or None, job_id=job_id)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'job_id': job_id
    }
    return render(request, 'job_application/create_job_app.html', context)

def edit_job_application(request):
    return render(request, 'job_application/edit_job_app.html')

def view_job_application(request):
    context = {
        'job_apps': JobApplication.objects.all()
    }
    return render(request, 'job_application/view_job_app.html', context)

def interview_help(request):
    return render(request, 'job_application/interview_help.html')