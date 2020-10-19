# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'job_application/home.html')

def create_job_application(request):
    return render(request, 'job_application/create_job_app.html')