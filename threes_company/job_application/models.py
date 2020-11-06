# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class JobApplication(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    education = models.TextField()
    skills = models.TextField()
    work_experience = models.TextField()
