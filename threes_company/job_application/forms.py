from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        job_id = kwargs.pop('job_id', 0)
        super(JobApplicationForm, self).__init__(*args, **kwargs)               # this will make sure the form is created before executing the next line
        self.fields['submitted_to'] = forms.CharField(initial=job_id)           # add a sumbitted_to field with initial value of job_id
        self.fields['submitted_to'].widget = forms.HiddenInput()                # hide the submitted_to input field
    class Meta:
        model = JobApplication
        fields = [
            'date_posted',
            'submitted_by',
            'education',
            'skills',
            'work_experience'
        ]
