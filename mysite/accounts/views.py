from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import login as auth_login
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'usersign.html', {'form': form})


def thesignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'thesign.html', {'form': form})


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)  # Django's login function
            return redirect('home.html')  # Redirect to success URL
        else:
            return render(request, 'userlog.html', {'error_message': 'Invalid credentials'})
        return render(request, 'userlog.html')


def thelogin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)  # Django's login function
            return redirect('home.html')  # Redirect to success URL
        else:
            return render(request, 'thelog.html', {'error_message': 'Invalid credentials'})
        return render(request, 'thelog.html')
def my_view(request):
    # Your view logic here
    return render(request, 'usersign.html')

def another_view(request):
    # Your view logic here
    return render(request, 'userlog.html')

def another_view1(request):
    # Your view logic here
    return render(request, 'thelog.html')

def another_view2(request):
    # Your view logic here
    return render(request, 'thesign.html')

