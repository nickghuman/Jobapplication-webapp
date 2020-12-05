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

@login_required
def edit_profile(request):
    user = User.objects.get(username=request.user)
    u_form = UserUpdateForm(request.POST or None, instance=user)
    
    # handles whether the user has or has not entered in their profile data yet
    try:
        profile = User_Profile.objects.get(user=user.id)
        p_form = UserProfileForm(request.POST or None, user=request.user, instance=profile)
    except User_Profile.DoesNotExist:
        p_form = UserProfileForm(request.POST or None, user=request.user)

    if request.method =='POST':
        if u_form.is_valid() and p_form.is_valid():
            profile = p_form.save()
            if request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            u_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('profile')
    else:
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'register/edit_profile.html', context )

@login_required
def create_profile(request):
    user = User.objects.get(username = request.user)
    p_form = UserProfileForm(request.POST or None, user= request.user, initial = dict(user=user.id))
    if p_form.is_valid():
        p_form.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('jobapp-home')
    else:
        context = {
            'p_form': p_form,
        }
        return render(request, 'register/create_profile.html', context)


    