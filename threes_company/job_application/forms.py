from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'date_posted',
            'submitted_by',
            'education',
            'skills',
            'work_experience'
        ]
