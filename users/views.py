from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, Profile
from .forms import LoginForm, SignupForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),
            )
            user.save()
            # Automatically log in the user after signup

            return redirect('profile', user_id=user.id)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        user=None
        if form.is_valid():
              email = form.cleaned_data['email']  
# Extract the email
              password = form.cleaned_data['password']  
              user = authenticate(request, email=email,password=password)
              print(user)
              
        if user is not None:
            print(user)
            print("user is authenticated")
            login(request, user)
            return redirect('/', user_id=user.id)
        else:
            form=LoginForm()
            return render(request, 'login.html', {'error': 'Invalid credentials','form': form})
    else:
      form = LoginForm()
            
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = Profile.objects.get(user=user)
    return render(request, 'profile.html', {'user': user, 'profile': profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
