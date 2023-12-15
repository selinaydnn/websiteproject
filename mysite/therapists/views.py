from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def therapist_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('account')
        else:
            return render(request, 'therapist_profile.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'therapist_profile.html')


def likeTherapist(request, therapist_id):
    therapist = get_object_or_404(therapist_profile(), pk=therapist_id)
    therapist.likes += 1
    therapist.save()
    # Redirect or return JSON response as needed

def dislikeTherapist(request, therapist_id):
    therapist = get_object_or_404(therapist_profile(), pk=therapist_id)
    therapist.dislikes += 1
    therapist.save()