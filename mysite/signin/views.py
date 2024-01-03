from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
# Create your views here.
