from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


def therapist_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Redirect to a success page or dashboard upon successful login
                return HttpResponseRedirect(reverse('therapists'))  # Replace 'dashboard' with your desired URL name
            else:
                # Handle inactive user
                pass  # You can add your logic here
        else:
            # Handle invalid login credentials
            pass  # You can add your logic here

    return render(request, 'thelogin/thelogin.html')
