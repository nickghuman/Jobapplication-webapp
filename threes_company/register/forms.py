from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user', 0)
        super(UserProfileForm, self).__init__(*args, **kwargs)               # this will make sure the form is created before executing the next line
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.all(), initial = User.objects.get(username = user_id))                 # add a sumbitted_to field with initial value of job_id
        self.fields['user'].widget = forms.HiddenInput()                # hide the submitted_to input field
    class Meta:
        model = User_Profile
        fields = [
                'user',
                'phone',
                'age',
                'address',
                'bio',
                'image'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name']



