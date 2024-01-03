from django.urls import path
from . import views

urlpatterns = [
    path('', views.therapist_signup, name='signup'),

]
