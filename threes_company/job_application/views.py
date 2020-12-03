# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm
from .models import JobApplication
import register
from .models import JobPosting

@login_required
def home(request):
    context = {
        'job_postings': JobPosting.objects.all()
    }
    return render(request, 'job_application/home.html', context)

@login_required
def create_job_application(request, job_id):
    form = JobApplicationForm(request.POST or None, job_id=int(job_id), initial=dict(submitted_by=request.user))
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'job_id': job_id
    }
    return render(request, 'job_application/create_job_app.html', context)

@login_required
def edit_job_application(request, job_app_id):
    job_app = JobApplication.objects.get(id=job_app_id)
    form = JobApplicationForm(request.POST or None, job_id=int(job_app.submitted_to_company.id), instance=job_app)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'job_app_id': job_app_id
    }
    return render(request, 'job_application/edit_job_app.html', context)

@login_required
def view_job_application(request):
    context = {
        'job_apps': JobApplication.objects.filter(submitted_by=request.user).select_related()
    }
    return render(request, 'job_application/view_job_app.html', context)

@login_required
def interview_help(request):
    return render(request, 'job_application/interview_help.html')

@login_required
def delete_job_application(reuqest, job_id=None):
    job_app_to_delete = JobApplication.objects.get(id=job_id)
    job_app_to_delete.delete()
    return redirect('/view/')