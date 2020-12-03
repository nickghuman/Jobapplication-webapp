from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import UserProfileForm , UserUpdateForm
from job_application import views
from .models import User_Profile

def login(request):
    return render(request, 'register/login.html')

def logout(request):
    return render(request, 'register/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
           # username = form.cleaned_data.get('username')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(request, new_user)
            return redirect('create_profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'register/profile.html')


def edit_profile(request):
    user = User.objects.get(username=request.user)
    profile = User_Profile.objects.get(user=user.id)
    u_form = UserUpdateForm(request.POST or None, instance=user)
    p_form = UserProfileForm(request.POST or None, user= request.user, instance=profile)
    if request.method =='POST':
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('profile')
    else:
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'register/edit_profile.html', context )

def create_profile(request ):
    user = User.objects.get(username = request.user)
    p_form = UserProfileForm(request.POST or None, user= request.user, initial = dict(user=user.id))
    if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('jobapp-home')
    else:
        context = {
            'p_form': p_form,
        }
        return render(request, 'register/create_profile.html', context)


    