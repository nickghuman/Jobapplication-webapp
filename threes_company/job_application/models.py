# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class JobPosting(models.Model):
    JOB_POST_STATUSES = [
        ('O', 'Open'),
        ('C', 'Closed'),
    ]
    date_posted = models.DateTimeField(default=timezone.now)
    company = models.CharField(max_length=60)
    job_position = models.CharField(max_length=60)
    status = models.CharField(max_length=1, choices=JOB_POST_STATUSES, default='O')
    description = models.TextField()

class JobApplication(models.Model):
    JOB_APP_STATUSES = [
        ('S', 'Sumbmitted'),
        ('U', 'Under Consideration'),
        ('N', 'No Longer Under Consideration'),
    ]
    date_posted = models.DateTimeField(default=timezone.now)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_to = models.ForeignKey(JobPosting, on_delete=models.CASCADE, default=1)
    education = models.TextField()
    skills = models.TextField()
    status = models.CharField(max_length=1, choices=JOB_APP_STATUSES, default='S')
    work_experience = models.TextField()

