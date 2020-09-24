from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! You Have Become An Author')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('Mini-Blog:home')
        else:
            form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    my_profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'my_profile': my_profile})

@login_required(login_url='login')
def edit_profile(request):
    my_profile = Profile.objects.get(user=request.user)
    user_profile = ProfileForm(instance=my_profile)
    user_form = UserForm(instance=request.user)
    if request.method == 'POST':
        user_profile = ProfileForm(request.POST, request.FILES, instance=my_profile)
        user_form = UserForm(request.POST, instance=request.user)
        if user_profile.is_valid() and user_form.is_valid():
            user_form.save()
            profile1 = user_profile.save(commit=False)
            profile1.user = request.user
            profile1.save()
            return redirect('accounts:profile')
        else:
            my_profile = Profile.objects.get(user=request.user)
            user_profile = ProfileForm(instance=my_profile)
    return render(request, 'accounts/profile_edit.html', {'user_profile': user_profile, 'user_form': user_form})
