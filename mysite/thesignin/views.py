from django.shortcuts import render
from .models import TherapistSignup
from django.http import HttpResponseRedirect

def therapist_signup(request):
    if request.method == 'POST':
        # Handle therapist sign-up form submission
        # Retrieve form data and create a new TherapistSignup object
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a new TherapistSignup object
        new_therapist = TherapistSignup(username=username, password=password)
        new_therapist.save()

        # Redirect to a success page or login page after sign-up
        #return HttpResponseRedirect('/thelogin/templates/thelogin.html/')  # Redirect to therapist login page

    return render(request, 'thesignup.html')  # Create therapist_signup.html template
