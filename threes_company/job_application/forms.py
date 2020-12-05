from django import forms
from .models import JobApplication
from .models import JobPosting

class JobApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        job_id = kwargs.pop('job_id', 0)
        super(JobApplicationForm, self).__init__(*args, **kwargs)                                                                                                       # this will make sure the form is created before executing the next line
        self.fields['submitted_to_company'] = forms.ModelChoiceField(queryset=JobPosting.objects.all(), initial=JobPosting.objects.get(id=int(job_id)))                 # add a sumbitted_to field with initial value of job_id
        self.fields['submitted_to_company'].widget = forms.HiddenInput()                                                                                                # hide the submitted_to input field
        self.fields['submitted_by'].widget = forms.HiddenInput()                                                                                                        # hide the submitted_by input field
        self.fields['date_posted'].widget = forms.HiddenInput()                                                                                                         # hide the date_posted input field
    class Meta:
        model = JobApplication
        fields = [
            'date_posted',
            'submitted_by',
            'submitted_to_company',
            'education',
            'skills',
            'work_experience'
        ]
