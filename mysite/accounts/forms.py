from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'last_name', 'email', 'password']

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']