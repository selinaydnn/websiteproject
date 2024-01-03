"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("accounts/", include("accounts.urls")),
    path("Questionnaire/",include("Questionnaire.urls")),
    path("therapists/", include("therapists.urls")),
    path("main_page/", include("main_page.urls")),
    path("About/", include('About.urls')),
    path("usersign/", views.signup, name='user_sign_up'),
    path("thesign/", views.thesignup, name='therapist_sign_up'),
    path("userlog/", views.login, name='user_log_in'),
    path("thelog/", views.thelogin, name='therapist_log_in'),


]
