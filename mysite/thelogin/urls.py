from django.urls import path
from . import views

urlpatterns = [
    path('thelogin/', views.therapist_login, name='therapist_login'),

]
