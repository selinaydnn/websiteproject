from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.therapist_profile, name='therapist_profile'),
    path('like/<int:therapist_id>/', views.likeTherapist, name='like_therapist'),
    path('dislike/<int:therapist_id>/', views.dislikeTherapist, name='dislike_therapist'),


]