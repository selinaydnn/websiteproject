from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


def therapist_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page after login
            return redirect('success_page')  # Replace 'success_page' with your success page URL name or path
        else:
            # Invalid credentials
            return render(request, 'thelogin.html', {'error_message': 'Invalid email or password'})

    return render(request, 'thelogin.html')
