from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.question, name='question'),
    path('submit/', views.submit_questionnaire, name='submit_questionnaire'),



]