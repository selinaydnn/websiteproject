from django.shortcuts import render,redirect

def index(request):
    return render(request,"base.html")

def signup(request):
    return render(request, "usersign.html")

def thesignup(request):
    return render(request, "thesign.html")

def login(request):
    return render(request, "userlog.html")

def thelogin(request):
    return render(request, "thelog.html")


def login_view(request):
    if user_logged_in_successfully:
        return redirect('therapist_profile')
    else:

        return render(request, 'userlog.html', {'error_message': 'Invalid credentials'})