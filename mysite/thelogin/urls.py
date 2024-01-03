from django.urls import path
from . import views

urlpatterns = [
    path('', views.therapist_login, name='thelogin'),

]
