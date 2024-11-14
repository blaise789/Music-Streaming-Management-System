from django import forms
# user creation form 
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm

class SignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=200)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ['email', 'password']
