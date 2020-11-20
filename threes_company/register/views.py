from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from job_application import views

def home(request):
    return render(request, 'jobapp-home')

def login(request):
    return render(request, 'register/login.html')

def logout(request):
    return render(request, 'register/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('jobapp-home')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'jobapp-home')
