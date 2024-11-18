from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import User, Profile

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered. Please use a different email.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter.")
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return confirm_password

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        max_length=200,
        validators=[EmailValidator(message="Enter a valid email address.")],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=128,
    )

    class Meta:
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if the email exists in the database
        if not User.objects.filter(email=email).exists():
            raise ValidationError("No account found with this email.")
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user and not user.check_password(password):
                raise ValidationError("Incorrect password.")
        return password
